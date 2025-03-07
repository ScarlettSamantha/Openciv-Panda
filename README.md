# SCiv

> 🚨 **Warning:** This project is in a very early development phase and is likely not functional yet. It may lack gameplay elements and is currently focused on testing raw system implementations.
> ⚠️ **Danger:** This code is highly dynamic and can be vulnerable to arbitrary remote code execution if modified or when using downloaded files. Malicious actors could exploit this to run harmful code(*!There is no sandbox!*). Be extremely cautious and only load trusted, verified sources.

## Running it

> Known Bugs: [Known Bugs](meta/known_bugs.md)

At the moment it will run *something* and I will attempt to keep the main branch booting into the "game" at the least.

### How to run it

Its not that hard to actually run it as its panda3d now.

```bash
git clone git@github.com:ScarlettSamantha/SCiv.git
cd SCiv
python3 -m venv .
bin/pip install -r requirements.txt
python3 main.py
```

### Debugging

You can connect it to pstats you need to have it listening on the default port `5185` then you press `p` to activate pstats broadcasting and `l` to stop it again.

In the `config.prc` is defined it will also debug GPU data but if this is causing issues you can disable it there.

#### Lenses

There are also lenses for debugging or you can use the buttons in the debug ui they will trigger the same functions.
Beware the menu and button states dont update each other tough

- `b`: Highlights units in `blue` while tiles that have no units in `red`
- `n`: Highlights resources and their types on the map `yellow` for strategic, `green`/`yellow` for bonus, `red` for none. please note colors might look different
- `m`: Highlights water and different types of it, `tiel` is coastal and shallow, `blue` deeper and sea
- `z`: Calculates and toggles major icons on tiles
- `x`: Toggles big buttons on tiles
- `c`: Toggles small icons on tiles

#### Issues

- Its reporting module missing: Please make a bug report forgot to add it to requirements.txt
- Why venv: Because if I tell you to break system packages and something goes wrong people get mad.

## Project

### 0.1.0 Goals

- [x] Have world render
- [x] Have resource system
- [x] Have ok atleast map generator
- [x] Manage entities
- [x] Spawn units
- [ ] Unit actions (WIP)
- [ ] Process a turn
- [ ] Cities that can build something
- ![ ] Basic UI element (WIP)
- [ ] Movement for units both pathfinded and weighted + UI (WIP)
- [x] Basic backend system integration like managers, systems, logging
- [x] Proper Implementation UI system (kivy)
- [ ] Units dumb fighting (no war or detection of rivers etc, just mele no range), meaby UI for this.

### Other information

- [Roadmap](meta/roadmap.md) - A rough roadmap (without timelines as this is a hobby project).
- [Contribution Guide](CONTRIBUTE.md) - Guidelines for contributing.
- [Changelog](CHANGELOG.md) - Automatically generated changelog.
- [File Structure](https://github.com/ScarlettSamantha/openciv-meta/blob/main/File%20Structure.md) - The project structure

<details>

<summary> <b>Progress</b> on systems: </summary>

|  System  |       Docs       |                             Name                              | Priority |             Expected Version Implementation              |    Thought out     |      Skeleton      | Basic Implementation |    Integration     |  UI   | Play  | Final Implementation | Balance |
| :------: | :--------------: | :-----------------------------------------------------------: | :------: | :------------------------------------------------------: | :----------------: | :----------------: | :------------------: | :----------------: | :---: | :---: | :------------------: | :-----: |
|  engine  | [\[doc\]](meta/) |             [Logging](openciv/engine/loading.py)              |          |         [v0.1 - PoC](./versions/0.0.1-poc.md)         | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  | :heavy_check_mark: |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |        [Resource Maths](openciv/gameplay/resource.py)         |          |         [v0.1 - PoC](./versions/0.0.1-poc.md)         | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |                [Ages](openciv/gameplay/age.py)                |          |         [v0.2 - PoC](./versions/0.0.1-poc.md)         |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |              [Saving](openciv/engine/saving.py)               |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |              [Loading](openciv/engine/saving.py)              |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |              [Tiles](openciv/gameplay/tiles.py)               |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |           [Yields](openciv/gameplay/tile_yield.py)            |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |            [Turn](openciv/engine/managers/turn.py)            |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |             [Combat](openciv/gameplay/combat.py)              |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |         [tile layers](openciv/engine/tile_layers.py)          |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |        [Graphics](openciv/engine/managers/graphics.py)        |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |          [Sounds](openciv/engine/managers/sound.py)           |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |        [Mod Support](openciv/engine/managers/mods.py)         |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |         [Land Plane](openciv/gameplay/planes/land.py)         |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |                [CPU AI](openciv/engine/ai.py)                 |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |        [Space Plane](openciv/gameplay/planes/space.py)        |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |         [Air Plane](openciv/gameplay/planes/land.py)          |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |        [Naval Plane](openciv/gameplay/planes/naval.py)        |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|  engine  | [\[doc\]](meta/) |     [Multiplayer](openciv/engine/managers/multiplayer.py)     |          | [1.1 - Multiplayer](./versions/1.1.0-multiplayer.md)  |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|    UI    | [\[doc\]](meta/) |    [Main Menu and Systems](openciv/engine/UI/main_menu.py)    |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|    UI    | [\[doc\]](meta/) | [Yield Overview](openciv/engine/UI/screens/yield_overview.py) |          |    [v0.4 - Alpha](./versions/0.2.0-development.md)    |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
|    UI    | [\[doc\]](meta/) |       [Options Menu](openciv/engine/UI/options_menu.py)       |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |            [Tech](openciv/engine/managers/tech.py)            |          |         [v0.1 - PoC](./versions/0.0.1-poc.md)         | :heavy_check_mark: | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |           [Textures](openciv/gameplay/textures.py)            |          |         [v0.1 - PoC](./versions/0.0.1-poc.md)         |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |   [Culture \(Civics\)](openciv/engine/managers/culture.py)    |          |         [v0.1 - PoC](./versions/0.0.1-poc.md)         | :heavy_check_mark: | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |              [Greats](openciv/gameplay/great.py)              |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |        [Victory Conditions](openciv/gameplay/victory)         |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Leaders](openciv/gameplay/leader.py)             |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |           [Civs](openciv/gameplay/civilization.py)            |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Effects](openciv/gameplay/effect.py)             |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |                [Tax](openciv/gameplay/tax.py)                 |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |          [Happiness](openciv/gameplay/happiness.py)           |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |         [Tile yields](openciv/gameplay/tile_yield.py)         |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Cities](openciv/gameplay/cities.py)              |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |               [Units](openciv/gameplay/unit.py)               |          | [v0.2 - Development](./versions/0.2.0-development.md) | :heavy_check_mark: | :heavy_check_mark: |  :heavy_check_mark:  |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |          [Events](openciv/gameplay/events/event.py)           |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Wonders](openciv/gameplay/wonder.py)             |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |           [Buildings](openciv/gameplay/building.py)           |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |            [Citizens](openciv/gameplay/citizen.py)            |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |                [Map](openciv/gameplay/map.py)                 |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |      [Goverments+Anarchy](openciv/gameplay/goverment.py)      |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |      [Ground Combat](openciv/gameplay/combat/ground.py)       |          | [v0.2 - Development](./versions/0.2.0-development.md) |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |               [Moods](openciv/gameplay/mood.py)               |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |       [Personalities](openciv/gameplay/personality.py)        |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Empire](openciv/gameplay/empire.py)              |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |              [Trade](openciv/gameplay/trade.py)               |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |              [Rivers](openciv/gameplay/river.py)              |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |        [Electricity](openciv/gameplay/electricity.py)         |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |          [Border Growth](openciv/gameplay/border.py)          |          |   [v0.3 - Pre-Alpha](./versions/0.3.0-pre-alpha.md)   |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |            [Climate](openciv/gameplay/climate.py)             |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |             [Gossip](openciv/gameplay/gossip.py)              |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |           [Alliances](openciv/gameplay/alliance.py)           |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |               [Spying](openciv/gameplay/spy.py)               |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |     [World Congress](openciv/gameplay/world_congress.py)      |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |            [Unit Items](openciv/gameplay/item.py)             |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |          [Influence](openciv/gameplay/influence.py)           |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |         [Air Combat](openciv/gameplay/combat/air.py)          |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |       [Naval Combat](openciv/gameplay/combat/naval.py)        |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |           [Satelites](openciv/gameplay/satelite.py)           |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |      [Advanced Diplomacy](openciv/gameplay/diplomacy.py)      |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |        [Unit Promotion](openciv/gameplay/promotion.py)        |          |       [v0.4 - Alpha](./versions/0.4.0-alpha.md)       |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |
| gameplay | [\[doc\]](meta/) |     [Dynamic Naming](openciv/gameplay/dynamic_naming.py)      |          |     [1.0 - Release](./versions/1.0.0-release.md)      |                    | :heavy_check_mark: |                      |                    |       |       |                      |         |

\*:Ready - Meaning that its in a state where I dont think it will need major work anymore just adjustments.
</div>
</details>

### Vision

> [Main document](meta/vision.md)

SCiv aims to create a larger and more complex game than Civilization VI, featuring a greater number of civilizations and deeper gameplay mechanics. Our goal is to build a game that retains the fun and engaging core gameplay of Civ6 while enhancing its complexity and mod-ability from the ground up. My aim is to create a more Stellaris-style Civ with more interesting things to do.

### Pitfalls

This is a lot of work, and the scale of the systems is significant. The main challenge might come from the lack of relevant game development experience. Currently, performance is acceptable, but we may need to revisit some aspects in the future. With careful planning and foresight, we hope to avoid major issues. But reality is almost never this good.

## Game

### Mechanics

- [Ages](./ideas/gameplay/age.md)
- [Climate](./ideas/gameplay/climate.md)
- [Disease](./ideas/gameplay/disease.md)
- [Yields](./ideas/gameplay/yields.md)
- [Movement](./ideas/gameplay/mechanics/movement.md)
- [Religion](./ideas/gameplay/mechanics/religion.md)

### Wonders

- [Early](./ideas/wonders/early.md)
- [Mid](./ideas/wonders/mid.md)
- [Late](./ideas/wonders/late.md)

### Greats

- [Artists](./ideas/gameplay/greats/artist.md)
- [Commercial](./ideas/gameplay/greats/commercial.md)
- [Folk Hero](./ideas/gameplay/greats/hero.md)
- [Holy](./ideas/gameplay/greats/faith.md)
- [Generals & Admirals](./ideas/gameplay/greats/military.md)
- [Engineers](./ideas/gameplay/greats/production.md)
- [Scientists](./ideas/gameplay/greats/science.md)

### Resources

| Resource          | Type                                                    | Code                                                  | Docs                                               |
| ----------------- | ------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------- |
| Bison             | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](resources/core/bonus/bison.py)                 | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Cheese            | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/cheese.py)                   | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Copper            | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/copper.py)                   | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Cows              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/cows.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Deer              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/deer.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Ember             | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/ember.py)                    | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Fish              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/fish.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Furs              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/furs.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Glass             | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/glass.py)                    | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Hardwood          | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/hardwood.py)                 | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Mercury           | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/murcury.py)                  | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Obsidian          | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/obsidian.py)                 | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Pigs              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/pigs.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Potato            | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/potato.py)                   | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Rice              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/rice.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Salt              | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/salt.py)                     | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Tin               | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/tin.py)                      | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Whales            | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/whales.py)                   | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Wheat             | [Bonus](meta/ideas/gameplay/resources/BONUS.md)         | [Code](ources/core/bonus/wheat.py)                    | [Docs](meta/ideas/gameplay/resources/BONUS.md)     |
| Cats              | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](ources/core/luxury/cats.py)                    | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Diamonds          | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](ources/core/luxury/diamonds.py)                | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Dogs              | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](ources/core/luxury/dogs.py)                    | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Gold              | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](ources/core/luxury/gold.py)                    | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Ivory             | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](ources/core/luxury/ivory.py)                   | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Jade              | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](resources/core/luxury/jade.py)                 | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Marble            | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](resources/core/luxury/marble.py)               | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Silver            | [Luxury](meta/ideas/gameplay/resources/LUXURY.md)       | [Code](resources/core/luxury/silver.py)               | [Docs](meta/ideas/gameplay/resources/LUXURY.md)    |
| Aluminium         | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/aluminium.py)         | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Coal              | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/coal.py)              | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Gas               | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/gas.py)               | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Graphite          | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/graphite.py)          | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Horses            | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/horses.py)            | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Oil               | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/oil.py)               | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Rare Earth Metals | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/rare_earth_metals.py) | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |
| Uranium           | [Strategic](meta/ideas/gameplay/resources/STRATEGIC.md) | [Code](resources/core/strategic/uranium.py)           | [Docs](meta/ideas/gameplay/resources/STRATEGIC.md) |

### Civilizations

| Civilization                                                  | Wikipedia Link                                                         | Code                                                     |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------- |
| [Akkadian](./ideas/civs/akkadian.md)               | [Akkadian Empire](https://en.wikipedia.org/wiki/Akkadian_Empire)       | [code](openciv/gameplay/civilization/akkadian.py)        |
| [American Empire](./ideas/civs/american_empire.md) | [American Empire](https://en.wikipedia.org/wiki/American_Empire)       | [code](openciv/gameplay/civilization/american_empire.py) |
| [Byzantine](./ideas/civs/byzantine.md)             | [Byzantine Empire](https://en.wikipedia.org/wiki/Byzantine_Empire)     | [code](openciv/gameplay/civilization/byzantine.py)       |
| [China](./ideas/civs/china.md)                     | [History of China](https://en.wikipedia.org/wiki/History_of_China)     | [code](openciv/gameplay/civilization/china.py)           |
| [Egypt](./ideas/civs/egypt.md)                     | [Ancient Egypt](https://en.wikipedia.org/wiki/Ancient_Egypt)           | [code](openciv/gameplay/civilization/egypt.py)           |
| [England](./ideas/civs/england.md)                 | [History of England](https://en.wikipedia.org/wiki/History_of_England) | [code](openciv/gameplay/civilization/england.py)         |
| [France](./ideas/civs/france.md)                   | [History of France](https://en.wikipedia.org/wiki/History_of_France)   | [code](openciv/gameplay/civilization/france.py)          |
| [Germany](./ideas/civs/germany.md)                 | [History of Germany](https://en.wikipedia.org/wiki/History_of_Germany) | [code](openciv/gameplay/civilization/germany.py)         |
| [Greece](./ideas/civs/greece.md)                   | [Ancient Greece](https://en.wikipedia.org/wiki/Ancient_Greece)         | [code](openciv/gameplay/civilization/greece.py)          |
| [Japan](./ideas/civs/japan.md)                     | [History of Japan](https://en.wikipedia.org/wiki/History_of_Japan)     | [code](openciv/gameplay/civilization/japan.py)           |
| [Korea](./ideas/civs/korea.md)                     | [History of Korea](https://en.wikipedia.org/wiki/History_of_Korea)     | [code](openciv/gameplay/civilization/korea.py)           |
| [Low Countries](./ideas/civs/low_countries.md)     | [Low Countries](https://en.wikipedia.org/wiki/Low_Countries)           | [code](openciv/gameplay/civilization/low_countries.py)   |
| [Ottoman](./ideas/civs/ottoman.md)                 | [Ottoman Empire](https://en.wikipedia.org/wiki/Ottoman_Empire)         | [code](openciv/gameplay/civilization/ottoman.py)         |
| [Persia](./ideas/civs/persia.md)                   | [Persian Empire](https://en.wikipedia.org/wiki/Persian_Empire)         | [code](openciv/gameplay/civilization/persia.py)          |
| [Rome](./ideas/civs/rome.md)                       | [Ancient Rome](https://en.wikipedia.org/wiki/Ancient_Rome)             | [code](openciv/gameplay/civilization/rome.py)            |
| [Spain](./ideas/civs/spain.md)                     | [History of Spain](https://en.wikipedia.org/wiki/History_of_Spain)     | [code](openciv/gameplay/civilization/spain.py)           |
| [USSR](./ideas/civs/ussr.md)                       | [Soviet Union](https://en.wikipedia.org/wiki/Soviet_Union)             | [code](openciv/gameplay/civilization/ussr.py)            |
| [Vikings](./ideas/civs/vikings.md)                 | [Vikings](https://en.wikipedia.org/wiki/Vikings)                       | [code](openciv/gameplay/civilization/vikings.py)         |

### Leaders

| Leader                                                                         | Wikipedia Link                                                                                       | Code                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Abraham Lincoln](./ideas/gameplay/leaders/abraham_lincoln.md)                 | [Abraham Lincoln (American Empire)](https://en.wikipedia.org/wiki/Abraham_Lincoln)                   | [code](openciv/gameplay/leaders/abraham_lincoln.py)         |
| [Alexander](./ideas/gameplay/leaders/alexander.md)                             | [Alexander the Great (Greece)](https://en.wikipedia.org/wiki/Alexander_the_Great)                    | [code](openciv/gameplay/leaders/alexander.py)               |
| [Ambiorix](./ideas/gameplay/leaders/ambiorix.md)                               | [Ambiorix (Low Countries)](https://en.wikipedia.org/wiki/Ambiorix)                                   | [code](openciv/gameplay/leaders/ambiorix.py)                |
| [Atatürk](./ideas/gameplay/leaders/attaturk.md)                                | [Mustafa Kemal Atatürk (Ottoman)](https://en.wikipedia.org/wiki/Mustafa_Kemal_Atat%C3%BCrk)          | [code](openciv/gameplay/leaders/attaturk.py)                |
| [Augustus](./ideas/gameplay/leaders/augustus.md)                               | [Augustus (Rome)](https://en.wikipedia.org/wiki/Augustus)                                            | [code](openciv/gameplay/leaders/augustus.py)                |
| [Caesar](./ideas/gameplay/leaders/caesar.md)                                   | [Julius Caesar (Rome)](https://en.wikipedia.org/wiki/Julius_Caesar)                                  | [code](openciv/gameplay/leaders/caesar.py)                  |
| [Charlemagne](./ideas/gameplay/leaders/charlemagne.md)                         | [Charlemagne (France)](https://en.wikipedia.org/wiki/Charlemagne)                                    | [code](openciv/gameplay/leaders/charlemagne.py)             |
| [Charles III](./ideas/gameplay/leaders/charles_iii.md)                         | [Charles III (Spain)](https://en.wikipedia.org/wiki/Charles_III_of_Spain)                            | [code](openciv/gameplay/leaders/charles_iii.py)             |
| [Charles V](./ideas/gameplay/leaders/charles_v.md)                             | [Charles V (Holy Roman Empire)](https://en.wikipedia.org/wiki/Charles_V,_Holy_Roman_Emperor)         | [code](openciv/gameplay/leaders/charles_v.py)               |
| [Cleopatra](./ideas/gameplay/leaders/cleopatra.md)                             | [Cleopatra (Egypt)](https://en.wikipedia.org/wiki/Cleopatra)                                         | [code](openciv/gameplay/leaders/cleopatra.py)               |
| [Cnut](./ideas/gameplay/leaders/cnut.md)                                       | [Cnut the Great (Vikings)](https://en.wikipedia.org/wiki/Cnut)                                       | [code](openciv/gameplay/leaders/cnut.py)                    |
| [Constantine](./ideas/gameplay/leaders/constantine.md)                         | [Constantine the Great (Byzantine)](https://en.wikipedia.org/wiki/Constantine_the_Great)             | [code](openciv/gameplay/leaders/constantine.py)             |
| [Darius](./ideas/gameplay/leaders/darius.md)                                   | [Darius the Great (Persia)](https://en.wikipedia.org/wiki/Darius_the_Great)                          | [code](openciv/gameplay/leaders/darius.py)                  |
| [De Gaulle](./ideas/gameplay/leaders/de_gaulle.md)                             | [Charles de Gaulle (France)](https://en.wikipedia.org/wiki/Charles_de_Gaulle)                        | [code](openciv/gameplay/leaders/de_gaulle.py)               |
| [Elizabeth](./ideas/gameplay/leaders/elizabeth.md)                             | [Elizabeth I (England)](https://en.wikipedia.org/wiki/Elizabeth_I)                                   | [code](openciv/gameplay/leaders/elizabeth.py)               |
| [FDR](./ideas/gameplay/leaders/fdr.md)                                         | [Franklin D. Roosevelt (American Empire)](https://en.wikipedia.org/wiki/Franklin_D._Roosevelt)       | [code](openciv/gameplay/leaders/fdr.py)                     |
| [Giovanni di Bicci de' Medici](./ideas/gameplay/leaders/goi.md)                | [Giovanni di Bicci de' Medici (Italy)](https://en.wikipedia.org/wiki/Giovanni_di_Bicci_de%27_Medici) | [code](openciv/gameplay/leaders/goi.py)                     |
| [Gorbachev](./ideas/gameplay/leaders/gorbashov.md)                             | [Mikhail Gorbachev (USSR)](https://en.wikipedia.org/wiki/Mikhail_Gorbachev)                          | [code](openciv/gameplay/leaders/gorbashov.py)               |
| [Herald](./ideas/gameplay/leaders/herald.md)                                   | [Herald of the Great Danelaw (Vikings)](https://en.wikipedia.org/wiki/Herald_of_the_Great_Danelaw)   | [code](openciv/gameplay/leaders/herald.py)                  |
| [Isabella](./ideas/gameplay/leaders/isabella.md)                               | [Isabella I of Castile (Spain)](https://en.wikipedia.org/wiki/Isabella_I_of_Castile)                 | [code](openciv/gameplay/leaders/isabella.py)                |
| [James](./ideas/gameplay/leaders/james.md)                                     | [James VI and I (England)](https://en.wikipedia.org/wiki/James_VI_and_I)                             | [code](openciv/gameplay/leaders/james.py)                   |
| [Joan van Oldenbarnevelt](./ideas/gameplay/leaders/joan_van_oldenbarnevelt.md) | [Johan van Oldenbarnevelt (Low Countries)](https://en.wikipedia.org/wiki/Johan_van_Oldenbarnevelt)   | [code](openciv/gameplay/leaders/joan_van_oldenbarnevelt.py) |
| [Justinian](./ideas/gameplay/leaders/justinian.md)                             | [Justinian I (Byzantine)](https://en.wikipedia.org/wiki/Justinian_I)                                 | [code](openciv/gameplay/leaders/justinian.py)               |
| [Kamehameha](./ideas/gameplay/leaders/kamehameha.md)                           | [Kamehameha I (Hawaii)](https://en.wikipedia.org/wiki/Kamehameha_I)                                  | [code](openciv/gameplay/leaders/kamehameha.py)              |
| [Kublai](./ideas/gameplay/leaders/kublai.md)                                   | [Kublai Khan (Mongolia)](https://en.wikipedia.org/wiki/Kublai_Khan)                                  | [code](openciv/gameplay/leaders/kublai.py)                  |
| [Lenin](./ideas/gameplay/leaders/lenin.md)                                     | [Vladimir Lenin (USSR)](https://en.wikipedia.org/wiki/Vladimir_Lenin)                                | [code](openciv/gameplay/leaders/lenin.py)                   |
| [Leonidas](./ideas/gameplay/leaders/leonidas.md)                               | [Leonidas I (Greece)](https://en.wikipedia.org/wiki/Leonidas_I)                                      | [code](openciv/gameplay/leaders/leonidas.py)                |
| [Louis XIV](./ideas/gameplay/leaders/louis.md)                                 | [Louis XIV (France)](https://en.wikipedia.org/wiki/Louis_XIV)                                        | [code](openciv/gameplay/leaders/louis.py)                   |
| [Meiji](./ideas/gameplay/leaders/meiji.md)                                     | [Meiji Emperor (Japan)](https://en.wikipedia.org/wiki/Meiji_(emperor))                               | [code](openciv/gameplay/leaders/meiji.py)                   |
| [Napoleon](./ideas/gameplay/leaders/napoleon.md)                               | [Napoleon Bonaparte (France)](https://en.wikipedia.org/wiki/Napoleon)                                | [code](openciv/gameplay/leaders/napoleon.py)                |
| [Naram-Sin](./ideas/gameplay/leaders/naram_sin.md)                             | [Naram-Sin (Akkadian)](https://en.wikipedia.org/wiki/Naram-Sin_of_Akkad)                             | [code](openciv/gameplay/leaders/naram_sin.py)               |
| [Nebuchadnezzar](./ideas/gameplay/leaders/nebuchadnezzar.md)                   | [Nebuchadnezzar II (Babylon)](https://en.wikipedia.org/wiki/Nebuchadnezzar_II)                       | [code](openciv/gameplay/leaders/nebuchadnezzar.py)          |
| [Otto](./ideas/gameplay/leaders/otto.md)                                       | [Otto von Bismarck (Germany)](https://en.wikipedia.org/wiki/Otto_von_Bismarck)                       | [code](openciv/gameplay/leaders/otto.py)                    |
| [Peter](./ideas/gameplay/leaders/peter.md)                                     | [Peter the Great (Russia)](https://en.wikipedia.org/wiki/Peter_the_Great)                            | [code](openciv/gameplay/leaders/peter.py)                   |
| [Philip II](./ideas/gameplay/leaders/phillip.md)                               | [Philip II of Spain (Spain)](https://en.wikipedia.org/wiki/Philip_II_of_Spain)                       | [code](openciv/gameplay/leaders/phillip.py)                 |
| [Qin Shi Huang](./ideas/gameplay/leaders/qin_shi_huang.md)                     | [Qin Shi Huang (China)](https://en.wikipedia.org/wiki/Qin_Shi_Huang)                                 | [code](openciv/gameplay/leaders/qin_shi_huang.py)           |
| [Ragnar](./ideas/gameplay/leaders/ragnar.md)                                   | [Ragnar Lodbrok (Vikings)](https://en.wikipedia.org/wiki/Ragnar_Lodbrok)                             | [code](openciv/gameplay/leaders/ragnar.py)                  |
| [Ramesses](./ideas/gameplay/leaders/ramesses.md)                               | [Ramesses II (Egypt)](https://en.wikipedia.org/wiki/Ramesses_II)                                     | [code](openciv/gameplay/leaders/ramesses.py)                |
| [Sargon](./ideas/gameplay/leaders/sargon.md)                                   | [Sargon of Akkad (Akkadian)](https://en.wikipedia.org/wiki/Sargon_of_Akkad)                          | [code](openciv/gameplay/leaders/sargon.py)                  |
| [Sejong](./ideas/gameplay/leaders/sejon.md)                                    | [Sejong the Great (Korea)](https://en.wikipedia.org/wiki/Sejong_the_Great)                           | [code](openciv/gameplay/leaders/sejon.py)                   |
| [Sitting Bull](./ideas/gameplay/leaders/sitting_bull.md)                       | [Sitting Bull (Sioux)](https://en.wikipedia.org/wiki/Sitting_Bull)                                   | [code](openciv/gameplay/leaders/sitting_bull.py)            |
| [Suleiman](./ideas/gameplay/leaders/suleiman.md)                               | [Suleiman the Magnificent (Ottoman)](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent)         | [code](openciv/gameplay/leaders/suleiman.py)                |
| [Taisho](./ideas/gameplay/leaders/taisho.md)                                   | [Taishō Emperor (Japan)](https://en.wikipedia.org/wiki/Taish%C5%8D_Emperor)                          | [code](openciv/gameplay/leaders/taisho.py)                  |
| [Tokugawa](./ideas/gameplay/leaders/tokugawa.md)                               | [Tokugawa Ieyasu (Japan)](https://en.wikipedia.org/wiki/Tokugawa_Ieyasu)                             | [code](openciv/gameplay/leaders/tokugawa.py)                |
| [Victoria](./ideas/gameplay/leaders/victoria.md)                               | [Queen Victoria (England)](https://en.wikipedia.org/wiki/Queen_Victoria)                             | [code](openciv/gameplay/leaders/victoria.py)                |
| [Wilhelm](./ideas/gameplay/leaders/wilhelm.md)                                 | [Wilhelm II (Germany)](https://en.wikipedia.org/wiki/Wilhelm_II,_German_Emperor)                     | [code](openciv/gameplay/leaders/wilhelm.py)                 |
| [William the Silent](./ideas/gameplay/leaders/willem.md)                       | [William the Silent (Low Countries)](https://en.wikipedia.org/wiki/William_the_Silent)               | [code](openciv/gameplay/leaders/willem.py)                  |
| [Wu Zetian](./ideas/gameplay/leaders/wu_zetian.md)                             | [Wu Zetian (China)](https://en.wikipedia.org/wiki/Wu_Zetian)                                         | [code](openciv/gameplay/leaders/wu_zetian.py)               |
| [Xerxes](./ideas/gameplay/leaders/xerxes.md)                                   | [Xerxes I (Persia)](https://en.wikipedia.org/wiki/Xerxes_I)                                          | [code](openciv/gameplay/leaders/xerxes.py)                  |

### Win Conditions

| Condition                                        | Mechanic                              | Meta-Docs                                           | Code |
| ------------------------------------------------ | ------------------------------------- | --------------------------------------------------- | ---- |
| [Alliance](./ideas/gameplay/victory/alliance.md) | State Building/Diplomacy              | [alliance.md](./ideas/gameplay/victory/alliance.md) | code |
| [Commerce](./ideas/gameplay/victory/gold.md)     | Gold/Corporations/Trade               | [gold.md](./ideas/gameplay/victory/gold.md)         | code |
| [Military](./ideas/gameplay/victory/military.md) | War/Military                          | [military.md](./ideas/gameplay/victory/military.md) | code |
| [Religion](./ideas/gameplay/victory/religion.md) | Religion/War/Spy/Instability          | [religion.md](./ideas/gameplay/victory/religion.md) | code |
| [Science](./ideas/gameplay/victory/science.md)   | State Building/Diplomacy              | [science.md](./ideas/gameplay/victory/science.md)   | code |
| [Culture](./ideas/gameplay/victory/culture.md)   | Culture/Tourism/Archaeology/Diplomacy | [culture.md](./ideas/gameplay/victory/culture.md)   | code |

> ⚖️ **Disclaimer:** This game and its associated code are provided for educational and informational purposes only. The author assumes no responsibility for any errors, omissions, or inaccuracies in the code. Users are strongly advised to thoroughly review, test, the code. The author makes no guarantees regarding the security, reliability, or performance of the game. By using this code, you agree that the author shall not be held liable for any damages, losses, or other consequences arising from its use, misuse, or inability to use the game, including but not limited to any unintended or harmful actions caused by the game. Use this game at your own risk and ensure that all necessary precautions are taken.
> 🌍 **Historical Context and Point of View Disclaimer:**
> OpenCiv includes civilizations, leaders, and events inspired by real-world history but real history is complex. While I strive to create a neutral point of view, the game may simplify or alter historical events for gameplay purposes. These portrayals try to not reflect any political or cultural stance but should not be taken as any kind of truth. The content reflects my personal view and understanding from a (inherently limited) Western perspective, and I try to avoid contentious topics I am uncomfortable with dealing with. I acknowledge that many events depicted were horrible and should never be repeated. This game is for entertainment. Please don't cancel me; I want to create a fun game for everyone. 🙏
