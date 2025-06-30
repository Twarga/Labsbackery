# 🥐 **LabsBakery** — *Figma‑style cyber‑lab builder*

> **Status:** ⛔ **Pre‑Alpha** (MVP cooking).  Expect bugs, missing docs, and the smell of fresh dough.

[![License: AGPL‑3.0](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)

---

## 1. What does this project do?

**LabsBakery** turns lab‑building into a three‑step recipe:

1. **Drag** virtual machines (Windows, Kali, Ubuntu…) onto a canvas.
2. **Draw** cables to show who talks to whom.
3. **Bake** — the app writes a *tiny* text file (`Vagrantfile` + `project.json`).  Share that file and anyone can run `vagrant up` to pull the images and spin the *exact same* lab.

Kilobytes shared, gigabytes downloaded on demand.  No disk shipping, no manual setup.

---

## 2. Why is this project useful?

I built LabsBakery as my **final‑year university project** because creating practice labs was the #1 pain in my own cyber‑security journey:

| Old pain                                                  | LabsBakery cure                                        |
| --------------------------------------------------------- | ------------------------------------------------------ |
| **Huge ISO downloads** for every assignment               | Re‑use cached cloud images                             |
| **Re‑creating VMs** again and again                       | Save a recipe, rebuild with one command                |
| **Costly cloud labs** (hard on a Moroccan student budget) | Run everything locally for free                        |
| **Sharing labs with classmates** was a mess               | Send one recipe file; teammates get an identical setup |

---

## 3. How do I get started?

```bash
# Clone
$ git clone https://github.com/twarga/LabsBakery.git && cd LabsBakery

# Backend
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload  # FastAPI

# Front‑end (Tailwind + Alpine.js)
$ npm install && npm run dev

# Open http://localhost:5173 and start baking!
```

> **Note:** Only Vagrant **≤ 2.3.7** (MPL‑2.0) is supported right now.  Run `vagrant --version` to check.

---

## 4. Need more help?

* **Docs** – full guide coming with v0.3.0.
* **Discussions** – [https://github.com/twarga/LabsBakery/discussions](https://github.com/twarga/LabsBakery/discussions)
* **Issues** – search first, then file.

---

## 5. Contributing

Right now we welcome **docs fixes, bug reports, and test cases**.  Feature PRs will open after the MVP lands.  See `CONTRIBUTING.md` (coming soon).

---

## 6. License

Code is **AGPL‑3.0‑or‑later**.  Public deployments must share their source.  Need a closed‑source exception? DM me on Twitter [@Twarga\_Dev](https://twitter.com/Twarga_Dev).

---

## 7. Roadmap (version‑based)

See [`ROADMAP.md`](ROADMAP.md).

---

Made with ❤ by **Twarga** — [@Twarga\_Dev](https://twitter.com/Twarga_Dev) · [https://twarga.tech](https://twarga.tech)
