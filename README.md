# Comics Daily 📰🎨
A collection of daily web comics from various sources.
## Latest Comics
*Last updated: 2025-12-04 22:06:43*
---
### [Extra Ordinary Comics](https://www.exocomics.com/)
**Date:** 2025-12-04
![Extra Ordinary Comics](src/exocomics-daily/data/2025-12-04/8-Oct-25_769.jpg)
---
### [Cyanide & Happiness](https://explosm.net/)
**Date:** 2025-12-03
![Cyanide & Happiness](src/explosm-daily/data/2025-12-03/2025-12-03_Kris Wilson.png)
---
### [Poorly Drawn Lines](https://poorlydrawnlines.com/)
**Date:** 2025-12-04
![Poorly Drawn Lines](src/poorlydrawnlines-daily/data/2025-12-04/understand-me.png)
---
### [Dinosaur Comics](https://qwantz.com/)
**Date:** 2025-12-04
![Dinosaur Comics](src/qwantz-daily/data/2025-12-04/comic2-5109.png)
---
### [Saturday Morning Breakfast Cereal](https://www.smbc-comics.com/)
**Date:** 2025-12-04
![Saturday Morning Breakfast Cereal](src/smbc-daily/data/2025-12-04/On the Edge.png)
---
### [XKCD](https://xkcd.com/)
**Date:** 2025-12-04
![XKCD](src/xkcd-daily/data/2025-12-04/Inverted Catenaries.png)
---

## About
This repository aggregates daily comics from multiple web comic sources. Each comic is automatically fetched and stored in its respective repository.

## Comic Sources
- [Extra Ordinary Comics](https://www.exocomics.com/) - [Repository](https://github.com/AI-Enthusiast/exocomics-daily)
- [Cyanide & Happiness](https://explosm.net/) - [Repository](https://github.com/AI-Enthusiast/explosm-daily)
- [Poorly Drawn Lines](https://poorlydrawnlines.com/) - [Repository](https://github.com/AI-Enthusiast/poorlydrawnlines-daily)
- [Dinosaur Comics](https://qwantz.com/) - [Repository](https://github.com/AI-Enthusiast/qwantz-daily)
- [Saturday Morning Breakfast Cereal](https://www.smbc-comics.com/) - [Repository](https://github.com/AI-Enthusiast/smbc-daily)
- [XKCD](https://xkcd.com/) - [Repository](https://github.com/AI-Enthusiast/xkcd-daily)

## Structure
```
comics-daily/
├── bin/           # Scripts and utilities
├── src/           # Comic repositories
│   ├── explosm-daily/
│   ├── xkcd-daily/
│   ├── exocomics-daily/
│   ├── smbc-daily/
│   ├── poorlydrawnlines-daily/
│   └── qwantz-daily/
└── README.md      # This file
```

## Usage
To clone all comic repositories:
```bash
./bin/init_pull.sh
```

To update this README with the latest comics:
```bash
python3 src/update_readme.md.py
```

---
*This README is automatically generated. Comics are property of their respective creators.*
