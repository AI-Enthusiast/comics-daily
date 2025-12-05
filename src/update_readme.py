#!/usr/bin/env python3
"""
Script to update the main README.md with the latest comic images from all web comic repositories.
Date: December 4, 2025
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, Tuple, List


def get_comic_repos(src_dir: Path) -> List[Path]:
    """Get all comic repository directories."""
    repos = []
    for item in src_dir.iterdir():
        if item.is_dir() and item.name.endswith('-daily') and (item / 'data').exists():
            repos.append(item)
    return sorted(repos)


def get_latest_comic(repo_path: Path) -> Optional[Tuple[str, Path, str]]:
    """
    Get the latest comic from a repository.
    Returns: (comic_name, image_path, date_folder) or None
    """
    data_dir = repo_path / 'data'
    if not data_dir.exists():
        return None

    # Get all date folders, sorted by name (which are in YYYY-MM-DD format)
    date_folders = [d for d in data_dir.iterdir() if d.is_dir()]
    if not date_folders:
        return None

    latest_folder = max(date_folders, key=lambda x: x.name)

    # Find the image file in the folder (look for .png, .jpg, .jpeg, .gif)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
    for ext in image_extensions:
        images = list(latest_folder.glob(f'*{ext}'))
        # Filter out metadata files
        images = [img for img in images if not img.name.endswith('_metadata.txt')]
        if images:
            # Use the first image found
            image_path = images[0]
            comic_name = repo_path.name.replace('-daily', '')
            return (comic_name, image_path, latest_folder.name)

    return None


def clean_data_directory(data_dir: Path) -> None:
    """Remove all files and directories from the data directory."""
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        return

    print(f"Cleaning data directory: {data_dir}")
    for item in data_dir.iterdir():
        if item.is_file():
            item.unlink()
            print(f"  - Removed: {item.name}")
        elif item.is_dir():
            shutil.rmtree(item)
            print(f"  - Removed directory: {item.name}")


def copy_comic_to_data(comic_name: str, image_path: Path, date: str, data_dir: Path) -> Path:
    """
    Copy a comic image to the central data directory.
    Returns: Path to the copied image
    """
    # Create a filename with format: comic-name_date.ext
    extension = image_path.suffix
    new_filename = f"{comic_name}_{date}{extension}"
    dest_path = data_dir / new_filename

    # Copy the file
    shutil.copy2(image_path, dest_path)
    print(f"  → Copied to: {dest_path.name}")

    return dest_path


def format_comic_name(name: str) -> str:
    """Format comic name for display."""
    # Map of internal names to display names
    name_map = {
        'explosm': 'Cyanide & Happiness',
        'xkcd': 'XKCD',
        'exocomics': 'Extra Ordinary Comics',
        'smbc': 'Saturday Morning Breakfast Cereal',
        'poorlydrawnlines': 'Poorly Drawn Lines',
        'qwantz': 'Dinosaur Comics'
    }
    return name_map.get(name, name.replace('_', ' ').title())


def get_comic_url(comic_name: str) -> str:
    """Get the official website URL for each comic."""
    url_map = {
        'explosm': 'https://explosm.net/',
        'xkcd': 'https://xkcd.com/',
        'exocomics': 'https://www.exocomics.com/',
        'smbc': 'https://www.smbc-comics.com/',
        'poorlydrawnlines': 'https://poorlydrawnlines.com/',
        'qwantz': 'https://qwantz.com/'
    }
    return url_map.get(comic_name, '#')


def generate_readme(comics_data: List[Tuple[str, Path, str]], project_root: Path) -> str:
    """Generate the README content."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    content = [
        "# Comics Daily 📰🎨\n",
        "A collection of daily web comics from various sources.\n",
        "## Latest Comics\n",
        f"*Last updated: {now}*\n",
        "---\n"
    ]

    for comic_name, image_path, date in comics_data:
        display_name = format_comic_name(comic_name)
        comic_url = get_comic_url(comic_name)

        # Create relative path from project root to image
        try:
            rel_path = image_path.relative_to(project_root)
        except ValueError:
            # If relative path fails, use absolute path
            rel_path = image_path

        content.extend([
            f"### [{display_name}]({comic_url})\n",
            f"**Date:** {date}\n",
            f"![{display_name}]({rel_path})\n",
            "---\n"
        ])

    content.extend([
        "\n## About\n",
        "This repository aggregates daily comics from multiple web comic sources. ",
        "Each comic is automatically fetched and stored in the central data directory.\n",
        "\n## Comic Sources\n"
    ])

    for comic_name, _, _ in comics_data:
        display_name = format_comic_name(comic_name)
        comic_url = get_comic_url(comic_name)
        repo_url = f"https://github.com/AI-Enthusiast/{comic_name}-daily"
        content.append(f"- [{display_name}]({comic_url}) - [Repository]({repo_url})\n")

    content.extend([
        "\n## Structure\n",
        "```\n",
        "comics-daily/\n",
        "├── bin/           # Scripts and utilities\n",
        "├── data/          # Latest comics (centralized)\n",
        "├── src/           # Comic scraper repositories\n",
        "│   ├── explosm-daily/\n",
        "│   ├── xkcd-daily/\n",
        "│   ├── exocomics-daily/\n",
        "│   ├── smbc-daily/\n",
        "│   ├── poorlydrawnlines-daily/\n",
        "│   └── qwantz-daily/\n",
        "└── README.md      # This file\n",
        "```\n",
        "\n## Usage\n",
        "To clone all comic repositories:\n",
        "```bash\n",
        "./bin/init_pull.sh\n",
        "```\n",
        "\nTo update this README with the latest comics:\n",
        "```bash\n",
        "python3 src/update_readme.py\n",
        "```\n",
        "\n---\n",
        "*This README is automatically generated. Comics are property of their respective creators.*\n"
    ])

    return ''.join(content)


def main():
    """Main function to update the README."""
    # Get paths
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    src_dir = project_root / 'src'
    data_dir = project_root / 'data'
    readme_path = project_root / 'README.md'

    print("🎨 Comics Daily README Updater")
    print("=" * 50)
    print(f"Project root: {project_root}")
    print(f"Source directory: {src_dir}")
    print(f"Data directory: {data_dir}")
    print(f"README path: {readme_path}")
    print()

    # Clean the data directory first
    clean_data_directory(data_dir)
    print()

    # Get all comic repositories
    repos = get_comic_repos(src_dir)
    print(f"Found {len(repos)} comic repositories:")
    for repo in repos:
        print(f"  - {repo.name}")
    print()

    # Get latest comic from each repository and copy to data directory
    comics_data = []
    for repo in repos:
        print(f"Processing {repo.name}...")
        latest = get_latest_comic(repo)
        if latest:
            comic_name, image_path, date = latest
            print(f"  ✓ Found latest comic: {image_path.name} ({date})")

            # Copy the comic to the central data directory
            new_path = copy_comic_to_data(comic_name, image_path, date, data_dir)

            # Store the new path instead of the original
            comics_data.append((comic_name, new_path, date))
        else:
            print(f"  ✗ No comics found")
    print()

    if not comics_data:
        print("❌ No comics found. Exiting.")
        return

    # Generate README content
    print("Generating README content...")
    readme_content = generate_readme(comics_data, project_root)

    # Write to file
    print(f"Writing to {readme_path}...")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print()
    print("✅ README.md successfully updated!")
    print(f"   {len(comics_data)} comics copied to {data_dir}")
    print()


if __name__ == '__main__':
    main()
