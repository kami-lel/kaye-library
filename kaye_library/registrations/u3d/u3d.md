# Unity Engine

Follows [Coder C Sharp](#coder-c-sharp)

Writing code based on [Coder](#coder)

Decode-only, never output the shorthand:

(((u3d-abbr)))

When naming an identifier, always use shorthand below over full word; decode any user writes:

(((u3d-identifier)))

Unity conventions:

- name code & assets per [Unity Naming](#unity-naming)
- pick a class role from [Common Type and Suffix](#common-type-and-suffix)
- write C# logic per [Unity Coding](#unity-coding)

  - expose fields per [Inspector Field](#inspector-field)
  - lay out a component per [MonoBehaviour](#monobehaviour)
  - lay out a data asset per [Scriptable Object](#scriptable-object)

- place assets & folders per [Assets Management](#assets-management)
- build prefabs & variants per [Prefab Usage](#prefab-usage)
- show & hide objects mid-run per [Owner-Driven Activation](#owner-driven-activation)
- move tuning values into data per [Game Tuning](#game-tuning)





## {description}

Sets baseline for all Unity 6 C# work, the shared root every topic-specific Unity skill builds on

## {when_to_use}

Any C# in a Unity project, even when user never says "Unity": gameplay, managers, editor tools, UI, save/load. Triggers: Unity, `UnityEngine`, `.cs` under `Assets/`, `MonoBehaviour`, `ScriptableObject`

## {globs}

```glob
**/*.cs
```

## {[Claude:Skill] Usage}

If needed, invoke `coder-c-sharp`, `coder`, `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-coding`, `u3d-if`, `u3d-mb`, `u3d-so`, `u3d-assets-management`, `u3d-pfb`, `u3d-owner-driven-activation`, or `u3d-game-tuning` skills via `Skill` tool.

## {[Hermes:skill_view] Usage}

If needed, load `coder-c-sharp`, `coder`, `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-coding`, `u3d-if`, `u3d-mb`, `u3d-so`, `u3d-assets-management`, `u3d-pfb`, `u3d-owner-driven-activation`, or `u3d-game-tuning` skills with `skill_view` tool.


































## Unity Naming

One convention names every noun-type thing: class, member, variable, file, GameObject, folder.

- Casing: code per [Coder](#coder); asset file, folder, and GameObject in [Pascal Case](#letter-case-pascal-case)
- Characters: no spaces or punctuation but the underscore, per [Underscore Usage](#underscore-usage)
- Order: subject first, qualifier after, so related names sort together (`HeroIdle`, `HeroRun`, never `IdleHero`)
- Subject: name what a thing is or serves, omitting what its folder, per [Assets Management](#assets-management), already says (`Ball.prefab`, `Rock.mat`, `ButtonClick.mp3`)
- Suffix: end a name with its role when one in [Common Type and Suffix](#common-type-and-suffix) fits
- Numbers: zero-pad (`Explosion_02`, `Explosion_10`)
- File Match: a script file takes strictly its class's name (`PlayerManager.cs` holds `PlayerManager`)
- Imported: an external asset (art, download, DAW export) keeps its arrival filename, since others define it
- Dev Copy: a private working copy takes `dev`, its owner's name, then the original name (`devJohnMain.unity` for `Main.unity`)





#### Unit Usage

Suffix a numeric name holding a physical quantity with its unit, by this shorthand:

(((u3d-units)))

- join units with `Per`, numerator first; a bare amount takes `Per` alone (`regenPerS`)
- apply to fields, locals, parameters, and getters (`MaxSpeedUPerS => maxSpeedUPerS`)
- leave a dimensionless value bare (ratio, count, multiplier), its range in the tooltip (`0~1`)
- end the field's tooltip with the same unit, per [Inspector Field](#inspector-field)

```csharp
[SerializeField]
[Tooltip("time stunned after a hit; s")]
private float hitStunDurationS = 0.4f;

[SerializeField]
[Tooltip("pull toward the anchor; u/s")]
private float pullSpeedUPerS = 3f;
```





#### Underscore Usage

The underscore carries these jobs, and no others:

- Key Prefix: a leading `_` sorts the key sibling first, a hub, base variant, or most used one, and takes no variant field (`_PopupBase.prefab`, `_Player.asset`)
- Variant or State: an inner `_` splits the subject from what tells one version of it apart, Pascal Case within each field (`Banana_Ripe.mat`, `Banana_Raw.mat`, `Player_Idle.anim`); use it whenever several things differ only by variant or state, such as two materials of one object, a sprite per state, or a prefab variant (`Popup_Confirm`, beside `_PopupBase`, per [Prefab Usage](#prefab-usage)); a further field may follow, such as a frame number or action (`Hero_Attack_01`)
- Channel: a texture map takes its channel as the variant field (`_Albedo`, `_Normal`), a packed map named for the channels it holds (`_MRA`)





### {description}

Names anything in a Unity project, code identifier or asset, so related things sort together & each name reads at a glance

### {when_to_use}

Naming or renaming anything in a Unity project, even unasked: new class, field, prefab, material, sprite, animation clip, folder. Triggers: "what to call this", rename, naming convention, variant, numbered asset

### {[Claude:Skill] Usage}

If needed, invoke `coder`, `style-letter-case-pascal-case`, `u3d-assets-management`, `u3d-common-type-and-suffix`, `u3d-if`, or `u3d-pfb` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `coder`, `style-letter-case-pascal-case`, `u3d-assets-management`, `u3d-common-type-and-suffix`, `u3d-if`, or `u3d-pfb` skills with `skill_view` tool.


































## Common Type and Suffix

Each type names a concept, not a script: give its suffix to whatever embodies that concept, be it a class, script or asset file, GameObject, prefab, or variable, its full name spelled per [Unity Naming](#unity-naming).

Scene Behaviour:

- Controller: drives one subject frame by frame, turning input or state into actions (`PlayerController`, `GameController`)
- Manager: owns one system's state for the whole run, exposing an API over it, never running a multi-step flow (`AccessoryManager`)
- Coordinator: runs one multi-step flow across several systems, in order (`LevelTransitionCoordinator`)
- Director: plays one authored timeline, firing content at scripted moments (`WaveDirector`)
- Spawner: decides where and when instances enter the scene, leaving construction to a Factory (`EnemySpawner`)

Entity Behaviour:

- Motor: turns a wanted direction or speed into velocity or force on one body (`CharacterMotor`)
- Sensor: detects what surrounds one entity and reports it, deciding nothing (`VisionSensor`)
- Ability: one activatable action of a character, with its own trigger, cost, and cooldown (`DashAbility`)
- Command: one action made an object, so it can be queued, replayed, or undone (`MoveCommand`)
- State: the behaviour of one state machine node (`PatrolState`)
- StateMachine: owns one entity's states and the transitions between them (`EnemyStateMachine`)
- Feedback: one burst of particles, sound, or camera shake, played on request (`HitFeedback`)

Event Delivery:

- Relay: passes one object's trigger or event callbacks on to an owner, holding no response logic (`DetectionZoneRelay`)
- Channel: one event pipe, so raiser and listener never reference each other (`GameOverEventChannel`)

Event Reaction:

- Listener: subscribes to one event source, a channel or a subject's event, and reacts on its own object (`PauseListener`)
- Binder: mirrors every state change of one known subject into its own object (`HealthBinder`)

World Object:

- Pickup: one collectible, handing its reward over once on touch (`BananaPickup`)
- Projectile: one thrown or fired thing, flying until it hits or expires (`CoconutProjectile`)
- Zone: one volume applying an effect to whatever is inside it (`SlowZone`)

Object Supply:

- Factory: creates and configures new instances of one type, hiding how (`EnemyFactory`)
- Pool: lends and reclaims reusable instances of one prefab, instead of instantiate and destroy (`BulletPool`)
- Registry: tracks live instances of one type, which register themselves, for lookup and iteration (`EnemyRegistry`)
- Generator: produces procedural content from rules and a seed (`LevelGenerator`)
- Provider: hands out one value or dependency on request, without owning its lifecycle (`InputProvider`)
- Service: logic behind an interface, with no scene presence and little or no state (`SaveService`)
- Loader: brings assets or scenes into memory, usually asynchronously (`SceneLoader`)

User Interface, shown & hidden per [Owner-Driven Activation](#owner-driven-activation):

- Screen: one full-screen interface, opening, closing, and owning its panels (`PauseScreen`)
- Panel: one self-contained region of a screen (`InventoryPanel`)
- Popup: a modal prompt shown over the current screen, then dismissed (`ConfirmPopup`)
- Toast: a timed, non-modal message shown over play, fading on its own, never blocking input (`HintToast`)
- Widget: a small reusable control with its own look and behaviour (`HealthBarWidget`)

MVP:

- Model: one feature's data and rules, ignorant of any display, raising events on change (`InventoryModel`)
- View: a passive display deciding nothing, exposing what to show and which input occurred (`InventoryView`); without a Presenter, use Panel or Widget
- Presenter: links one Model to one View, so neither knows the other (`InventoryPresenter`)

Authored Data, chosen per [Game Tuning](#game-tuning), shaped per [Scriptable Object](#scriptable-object):

- Config: tunable values, read by whatever it configures (`AudioConfig`)
- Definition: the authored content of one thing, read-only at runtime (`WeaponDefinition`)
- Setting: options the player or project chooses, apart from a Config's designer tuning (`GraphicsSetting`)
- Catalog: every Definition of one kind, collected for lookup by id (`ItemCatalog`)
- Preset: named values bundled to apply in one step (`DifficultyPreset`)
- Save: a record of progress, persisted to disk (`PlayerSave`)





### {description}

Assigns each Unity class, script, GameObject, or asset one architectural role, so responsibilities split cleanly & its name says what it does

### {when_to_use}

Designing a Unity system or deciding what a new class should own, even when user only asks "manager or controller?": splitting a god class, picking a pattern, reviewing a misnamed script. Triggers: manager, controller, architecture, responsibility, design pattern, MVP, event pipe, "what should this class be"

### {[Claude:Skill] Usage}

If needed, invoke `u3d-naming`, `u3d-owner-driven-activation`, `u3d-game-tuning`, or `u3d-so` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-naming`, `u3d-owner-driven-activation`, `u3d-game-tuning`, or `u3d-so` skills with `skill_view` tool.


































## Unity Coding

- `var` only for a `foreach` local or a long generic right-hand side
- singleton: expose the instance through a static member named exactly `I` (`GamepadManager.I`)
- events: prefer the C# `event` keyword over `UnityEvent` (`public event Action<int> HealthChanged;`)
- member order in a plain class: `[SerializeField]` fields, public API, plain fields, private helpers, constructor last; a `MonoBehaviour` follows [MonoBehaviour](#monobehaviour), a `ScriptableObject` [Scriptable Object](#scriptable-object)
- serialized fields: declare per [Inspector Field](#inspector-field)
- gameplay numbers: keep in data per [Game Tuning](#game-tuning), never as literals
- banners per [Comment Banner](#comment-banner), laid out as the example shows, and none at all in a small or single-purpose file
- name every class, member, and variable per [Unity Naming](#unity-naming), suffixed per [Common Type and Suffix](#common-type-and-suffix) and [Unit Usage](#unit-usage)



#### Input

Read gameplay input through the Input System: `InputAction`s from an Input Actions asset, kept in `Inputs/` per [Assets Management](#assets-management), never a keyboard, mouse, or gamepad directly. Express timing, such as a double-tap, as an interaction (`MultiTap`), never as a hand-rolled key tracker



#### Logging

Log every meaningful state change so a debug session reads as a sequence of events: lifecycle transitions, branch decisions, external calls (network, save/load, scene loads).

Open every message with the owning subsystem or module name, a colon, and a tab.

Warning and error are reserved for a failed guard clause, such as the Inspector Assignment Guard in [MonoBehaviour](#monobehaviour). Every other log is debug level, gated by `Debug.isDebugBuild` and braced even for one statement.

```csharp
private void Awake() {
    if (rb == null) {
        Debug.LogError("Inventory:\tfail to get Component: Rigidbody2D", this);
    }
    if (itemPrefab == null) {
        Debug.LogWarning(
            "Inventory:\tmust assign Inspector Field: Item Prefab", this);
    }
    if (Debug.isDebugBuild) {
        Debug.Log("Inventory:\tready");
    }
}
```





### {description}

Writes, edits & reviews Unity C# logic in house idiom, so code reads consistently & a debug session traces as a sequence of events

### {when_to_use}

Writing or reviewing any Unity C# behaviour, even when user only asks for a feature: game logic, input handling, events, singletons, debug output. Triggers: `Debug.Log`, `InputAction`, singleton, event, "add logging", "read input"

### {[Claude:Skill] Usage}

If needed, invoke `u3d-mb`, `u3d-so`, `u3d-if`, `u3d-game-tuning`, `coder-comment-banner-in-code-comment`, `u3d-naming`, `u3d-common-type-and-suffix`, or `u3d-assets-management` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-mb`, `u3d-so`, `u3d-if`, `u3d-game-tuning`, `coder-comment-banner-in-code-comment`, `u3d-naming`, `u3d-common-type-and-suffix`, or `u3d-assets-management` skills with `skill_view` tool.













### Inspector Field

Applies to every serialized field of a [MonoBehaviour](#monobehaviour) or [Scriptable Object](#scriptable-object), each named per [Unity Naming](#unity-naming).

- declare as `[SerializeField] private`, never a public field
- prefer `[Tooltip]` on each field, worded in briefness style, ending with its unit per [Unit Usage](#unit-usage)
- prefer `[Header]` dividing fields into groups
- put a simple numeric bound in `[Min]` or `[Range]`; `OnValidate` only for a rule they cannot state
- add `[RequireComponent]` on a class that reads a sibling component
- add `[FormerlySerializedAs]` on a renamed field, keeping its saved values

```csharp
[RequireComponent(typeof(Rigidbody2D))]
public class CharacterMotor: MonoBehaviour {
    [Header("Movement")]
    [SerializeField]
    [Tooltip("top speed; u/s")]
    [Min(0f)]
    private float maxSpeedUPerS = 5f;

    [SerializeField]
    [FormerlySerializedAs("jumpPower")]
    [Tooltip("launch speed of a jump; u/s")]
    private float jumpSpeedUPerS = 8f;
}
```



#### {description}

Declares Unity Inspector fields so designers read, tune & rename them without breaking saved values

#### {when_to_use}

Adding, renaming, or reviewing any value exposed in the Inspector, even when user only says "expose this" or "make it tweakable". Triggers: `[SerializeField]`, Inspector, public field, "show in editor", tooltip

#### {[Claude:Skill] Usage}

If needed, invoke `u3d-mb`, `u3d-so`, or `u3d-naming` skills via `Skill` tool.

#### {[Hermes:skill_view] Usage}

If needed, load `u3d-mb`, `u3d-so`, or `u3d-naming` skills with `skill_view` tool.













### MonoBehaviour

Section order, formatting, and accessors follow the example exactly.

Name the class and its members per [Unity Naming](#unity-naming), its role suffix per [Common Type and Suffix](#common-type-and-suffix); declare fields per [Inspector Field](#inspector-field); toggle a short-lived object per [Owner-Driven Activation](#owner-driven-activation).

Inspector Assignment Guard:

- guard **every** `[SerializeField] private` field carrying no declaration default (`private string label = "default";` needs none)
- **one block, at the top** of `Awake()`, under exactly one `// Inspector Assignment Guard` line, never scattered, never repeated
- word each failed guard per [Logging](#logging)

```csharp
public class PlayerController: MonoBehaviour {
    // Public Members  #########################################################
    public GameState currentState;

    // Public Methods  #########################################################
    public static PlayerController FindInScene() { ... }

    // Inspector Fields  #######################################################
    ~~~

    // MonoBehaviour Lifecycle  ################################################
    private void Awake() {
        // Inspector Assignment Guard  -----------------------------------------
        if (nextSceneName == null) {
            Debug.LogWarning(
                "MinigameRacing:\tmust assign Inspector Field: nextSceneName",
                this);
        }
        ...  // other guards, then other code
    }
    private void Start() { ... }

    // Event Handlers  #########################################################
    private void OnSceneLoaded(Scene scene, LoadSceneMode mode) { ... }

    // constants  ##############################################################
    private const string LOAD_TRIGGER_TAG = "LoadNextSceneTrigger";

    // private members  ########################################################
    private float startVelocityX;

    // cached references  ------------------------------------------------------
    private Rigidbody2D body;

    // private methods  ########################################################
    private void PlayIntroSequence() { ... }
}
```



#### {description}

Structures Unity `MonoBehaviour` scripts in one fixed layout, so every component reads alike & missing Inspector assignments surface at startup

#### {when_to_use}

Any Unity script attached to a GameObject, the default shape of most gameplay code, even when user never names `MonoBehaviour`: player, enemy, trigger zone, camera rig, UI behaviour. Triggers: `MonoBehaviour`, `Awake`, `Update`, `OnTriggerEnter`, `GetComponent`, "add a component"

#### {[Claude:Skill] Usage}

If needed, invoke `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-if`, `u3d-owner-driven-activation`, or `u3d-coding` skills via `Skill` tool.

#### {[Hermes:skill_view] Usage}

If needed, load `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-if`, `u3d-owner-driven-activation`, or `u3d-coding` skills with `skill_view` tool.













### Scriptable Object

Section order, formatting, and accessors follow the example exactly.

Name the class per [Unity Naming](#unity-naming), its role suffix per [Common Type and Suffix](#common-type-and-suffix); declare fields per [Inspector Field](#inspector-field); decide which values it holds per [Game Tuning](#game-tuning).

Menu Path:

- one `[CreateAssetMenu]` per class, `menuName` always `"Scriptable Objects/<ClassName>"`

Data Access:

- every serialized field is `private`, exposed through a read-only `=>` getter under Public Members, documented with `<returns>`
- no public mutable field and no setter: asset data is read-only at runtime, since an edit made in Play mode would persist in the asset

Editor Validation:

- `OnValidate` sits last under an `// Editor Validation` banner, keeping a rule an attribute cannot state (a cross-field bound)
- no `Awake` and no Inspector Assignment Guard: a Config's fields all carry declaration defaults

```csharp
[CreateAssetMenu(menuName = "Scriptable Objects/PlayerBalanceConfig")]
public class PlayerBalanceConfig: ScriptableObject {
    // Public Members  #########################################################
    /// <returns>slowest allowed speed; u/s</returns>
    public float MinSpeedUPerS => minSpeedUPerS;
    /// <returns>top speed; u/s</returns>
    public float MaxSpeedUPerS => maxSpeedUPerS;

    // Inspector Fields  #######################################################
    ~~~

    // Editor Validation  ######################################################
    private void OnValidate() {
        maxSpeedUPerS = Mathf.Max(minSpeedUPerS, maxSpeedUPerS);
    }
}
```



#### {description}

Structures Unity `ScriptableObject` classes in one fixed layout, keeping asset data read-only & valid at runtime

#### {when_to_use}

Any designer-editable data living outside a scene, even when user only says "config", "settings", "database", "shared data": level config, item stats, event channel. Triggers: `ScriptableObject`, `CreateAssetMenu`, `.asset`, data container

#### {[Claude:Skill] Usage}

If needed, invoke `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-if`, or `u3d-game-tuning` skills via `Skill` tool.

#### {[Hermes:skill_view] Usage}

If needed, load `u3d-naming`, `u3d-common-type-and-suffix`, `u3d-if`, or `u3d-game-tuning` skills with `skill_view` tool.































## Assets Management

Everything authored lives under one underscore-prefixed root named for the game, `Assets/_MyGame/`, sorting above Unity's own and vendor folders. Paths below are relative to it, and that prefix repeats on any folder that should lead its listing.

A file's path reads in up to 3 levels under the root, so any file is found without search:

- Asset Type: what the file is (`Scripts/`, `Prefabs/`), always present
- Asset Domain: which area of the game it serves (`Mobs/`, `World/`), optional
- Asset Module: which scene or subsystem owns it (`Spider/`, `MinigameRacing/`), the same name in every asset type

```
Assets/_MyGame/Scripts/Mobs/Spider/SpiderController.cs
Assets/_MyGame/Prefabs/Mobs/Spider/Spider.prefab
Assets/_MyGame/Textures/MinigameRacing/StartFlag.png
```

Name every asset file, folder, and GameObject per [Unity Naming](#unity-naming).





#### Asset Types

One level under the root:

- `Scripts/`: C#
- `Audio/`: music and effects, split into its own domains, per the audio-only domains below
- `Sprites/`, `Textures/`: 2D art, where split: `Sprites/` gameplay-facing, `Textures/` the rest
- `Animations/`: `.anim` clips, `.controller` graphs
- `Prefabs/`: prefabs, made per [Prefab Usage](#prefab-usage)
- `Scenes/`: `.unity` files, optionally nested by area (`Scenes/Minigames/`)
- `Materials/`, `Tilemaps/`: 2D and tilemap work
- `Meshes/`: 3D model and `.mesh` assets
- `Plugins/`
- `Settings/`: project-level `.asset` files
- `Localizations/`: locale and string-table assets
- `Shaders/`: `.shader`, `.shadergraph`, `.hlsl` files
- `Fonts/`: font files and their `.asset` font settings
- `Inputs/`: `.inputactions` assets
- `VFXs/`: particle systems and Visual Effect Graph assets
- `Timelines/`: `.playable` Timeline assets





#### Asset Domains

A domain folder sits between an asset type and its modules, gathering the modules of one kind (`Scripts/Mobs/Spider/`). Use one once an asset type holds several modules of that kind; leave a small asset type flat.

- reuse the same domain name in every asset type holding its assets, like a module name
- spell it out in [Pascal Case](#letter-case-pascal-case), never abbreviate
- plural for a domain holding many (`Mobs`, `Items`, `Cameras`), singular for a one-of-a-kind (`Player`, `World`, `UI`)
- place a module by what it does in play, so a thrown coconut goes under `Combat` or `Items`, not both
- add a domain only when it names one clear responsibility, decidable at a glance

Common domains:

- `Mobs/`: hostile creatures the player fights or avoids
- `World/`: the playable space and its scenery, from terrain and props to level logic
- `Cameras/`: camera rigs and their behaviours
- `Items/`: collectibles and carried things
- `Player/`: the player character
- `UI/`: screens, panels, and HUD
- `Combat/`: damage, health, and hit logic shared by everything that fights
- `Interactables/`: things the player activates, such as doors, levers, and chests

Audio-only domains, valid under `Audio/` alone and never elsewhere:

- `BGMs/`: background music tracks, module subfolders (eg `Audio/BGMs/Lv1/`)
- `SFXs/`: sound effects, module subfolders, or effect-family subfolders for effects spanning every module (eg `Audio/SFXs/PlayerHit/`)





#### Asset Modules

One short [Pascal Case](#letter-case-pascal-case) name per scene/subsystem, reused identically in every asset type holding its assets: the module name is the constant, the asset type changes around it. Spell it out, never abbreviate. Where modules form a family, the family word leads so the family sorts together:

- Family Member: `MinigameRacing`, `MinigameHiking`, `MinigameHideNSeek`
- Level: `Lv1`, `Lv2`, numbered rather than named
- Screen: `StartScreen`, `PauseScreen`, `SettingsScreen`, every full-screen interface taking the word `Screen`
- Standalone Module: `SaveSystem`, `Inventory`, sharing a name with nothing else
- `_Shared/`: the module slot taken by whatever no single module owns, sorting first on its underscore prefix





### {description}

Places Unity assets & folders across `Assets/`, so any file is found by asset type, domain & module without search

### {when_to_use}

Creating, moving, importing any Unity asset, even when user never mentions folder: new script file, scene, prefab, audio clip, texture, animation. Triggers: "where does this go", folder layout, project structure, `Assets/`, import, organize

### {[Claude:Skill] Usage}

If needed, invoke `u3d-naming`, `u3d-pfb`, or `style-letter-case-pascal-case` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-naming`, `u3d-pfb`, or `style-letter-case-pascal-case` skills with `skill_view` tool.



































## Prefab Usage

Reach for prefabs extensively: turn an object into a prefab as soon as a reason below holds, progressively as the project grows, rather than waiting for a cleanup pass. Store each under `Prefabs/` per [Assets Management](#assets-management).

Make a prefab when:

- 2 or more objects are copies or variants of each other
- the object could be reused elsewhere, such as in another scene, even if it is used once today

Prefer the base and variant pattern for a family of near-identical objects:

- base prefab: holds everything the family shares, named with a leading `_`, the subject, and `Base` (`_PopupBase.prefab`)
- variant prefab: a Prefab Variant of the base, overriding only what differs, named per [Underscore Usage](#underscore-usage) (`Popup_Confirm.prefab`)
- put a change shared by the whole family in the base, so every variant follows it
- a scene holds instances of the prefab, never a hand-made copy of one





### {description}

Turns Unity scene objects into prefabs & variant families early, so one edit updates every copy

### {when_to_use}

Building, duplicating, or reviewing scene objects, even when user never says "prefab": copy-pasted GameObjects, a 2nd enemy type, reusable popup, near-identical variants. Triggers: prefab, Prefab Variant, duplicate, reuse, "same as that one but"

### {[Claude:Skill] Usage}

If needed, invoke `u3d-assets-management` or `u3d-naming` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-assets-management` or `u3d-naming` skills with `skill_view` tool.


































## Owner-Driven Activation

Save a GameObject inactive when it lives for only a stretch of the run; let an owner, such as a Screen, Coordinator, or Pool per [Common Type and Suffix](#common-type-and-suffix), call `SetActive`, with no `Update` flag guards

Apply to:

- UI: pause screen, game over screen, settings panel, tutorial overlay, popup, toast, tooltip
- spawned or pooled: enemy, projectile, pickup, hit flash, particle effect, decal
- scripted: cutscene prop, event actor, boss arena gate, tutorial arrow
- mode-specific: alternate camera, debug panel, editor-only stand-in
- streamed: level section loaded in and out by distance or progress

Don't apply to:

- manager, singleton, event hub, listener
- camera follow, input reader, audio mixer
- the owner itself

Rules:

- hold each target in a `[SerializeField]` reference on the owner, declared per [Inspector Field](#inspector-field), never find it by search
- subscribe and reset in `OnEnable`, unsubscribe in `OnDisable`
- give each target one entry point (`Show`, `Hide`), and call only that from the owner
- assign each toggled group exactly one owner
- rest each object in its original active state: a screen is saved inactive and switched on by its owner, a manager is saved active and stays so
- toggle component `enabled`, a child visual, or `CanvasGroup` instead when the object must stay findable or listening
- play a hide state before `SetActive(false)` when the object needs an exit animation





### {description}

Controls Unity GameObjects living only part of a run through one owner, so showing, hiding & spawning stay predictable & cost nothing while idle

### {when_to_use}

Showing, hiding, spawning, or enabling objects mid-run, even when user only says "open the menu" or "turn it on": pause screen, popup, toast, pooled enemy, cutscene prop. Triggers: `SetActive`, show/hide, enable/disable, toggle, "appear when"

### {[Claude:Skill] Usage}

If needed, invoke `u3d-common-type-and-suffix` or `u3d-if` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-common-type-and-suffix` or `u3d-if` skills with `skill_view` tool.

























## Game Tuning

Prefer tunable gameplay numbers in data over code (speed, damage, cooldown, spawn rate, ramp): a designer can then adjust them in the Inspector, even in Play mode, without a recompile. A structural constant (a tag, a layer, an array size) is not tuning, and a `const` suits it.

Tuning leans on three objects, each per its [Common Type and Suffix](#common-type-and-suffix) role, each class shaped per [Scriptable Object](#scriptable-object):

- Config: SO holding the tuning values of one concern, the core structure of tuning (`PlayerBalanceConfig`)
- Definition: SO holding what one thing is, its identity and own stats, one asset per thing (`WeaponDefinition`)
- Preset: bundle of named values applied to a Config in one step, eg a difficulty tier (`DifficultyPreset`)

Config vs Definition: a Config answers how a system behaves, a Definition answers what a thing is. A value shared by every instance of a system tends to suit a Config; a value that differs per thing tends to suit its Definition.

Config leanings:

- one Config per concern, with balance split into a few assets (player, world, enemy) rather than one asset for everything or one asset per field
- a reader holds a `[SerializeField]` for the one Config it needs, rather than a hub asset reaching every concern
- treat a Config as read-only at runtime: a reader can copy a value into its own state before changing it, since an edit made in Play mode would persist in the asset
- expose each private serialized field as a read-only `=>` getter
- clamp in `OnValidate` under an `// Editor Validation` banner, so an out-of-range value does not reach play
- let one reader own the meaning of each value; a second reader of the same value can ask the Config instead of keeping its own copy
- let a Preset overwrite Config values through its single apply entry point rather than from scattered code





#### Tuning with AnimationCurve

Reach for an `AnimationCurve` extensively when a value depends on another value, in place of a formula or a table of constants: difficulty ramping, falloff by distance, damage by charge, speed by health fraction, reward by streak. The designer draws the curve, so its shape can change without code.

Common x axes:

- elapsed time of a run or an encounter
- difficulty level or wave number
- normalized progress, 0~1
- distance, health fraction, stack count

Preferences:

- name the field `<Value>Curve` and state both axes with units per [Unit Usage](#unit-usage) in its `[Tooltip]`, x first (`x: ramp progress 0~1; y: spawn interval; s`)
- normalize x to 0~1 when its range varies, and keep the range in a separate Config field (a ramp duration), so one curve serves any length
- hide `Evaluate` behind a Config method that clamps x (`GetIntervalS(elapsedS)`), so a reader need not touch the curve
- give a curve a non-empty initializer (`AnimationCurve.Linear`), since an unset curve evaluates to 0 and silently zeroes the value
- let the y axis be a multiplier on a base value when one curve shapes several values, and absolute when it shapes one
- a plain float still suits a value that depends on nothing

```csharp
[CreateAssetMenu(menuName = "Scriptable Objects/SpawnBalanceConfig")]
public class SpawnBalanceConfig: ScriptableObject {
    // Public Members  #########################################################
    public float GetIntervalS(float elapsedS) =>
        intervalCurve.Evaluate(Mathf.Clamp01(elapsedS / rampDurationS));

    // Inspector Fields  #######################################################
    ~~~
}
```





### {description}

Moves Unity gameplay numbers out of code into designer-editable data, so balance changes need no recompile

### {when_to_use}

Any tunable gameplay value, even unasked: speed, damage, cooldown, spawn rate, difficulty ramp, hard-coded magic number. Triggers: balance, tuning, difficulty, curve, "let the designer tweak", magic number

### {[Claude:Skill] Usage}

If needed, invoke `u3d-common-type-and-suffix`, `u3d-so`, or `u3d-naming` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

If needed, load `u3d-common-type-and-suffix`, `u3d-so`, or `u3d-naming` skills with `skill_view` tool.
