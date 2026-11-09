# Unity Engine

Follows [Coder C Sharp](#coder-c-sharp)

Writing code based on [Coder](#coder)

Decode-only, never output the shorthand:

(((u3d-abbr)))

When naming an identifier, always use shorthand below over full word; decode any user writes:

(((u3d-identifier)))



#### coding for unity engine

- `var` only for a `foreach` local or a long generic right-hand side
- singleton: expose the instance through a static member named exactly `I` (`GamepadManager.I`)
- events: prefer the C# `event` keyword over `UnityEvent` (`public event Action<int> HealthChanged;`)
- member order in a plain class: `[SerializeField]` fields, public API, plain fields, private helpers, constructor last; a `MonoBehaviour` follows its own example below
- banners per [Comment Banner](#comment-banner), laid out as the example shows, and none at all in a small or single-purpose file



#### class naming

Suffix each class name by its role:

Scene Behaviour:

- Controller: script driving one subject frame by frame, turning input or state into actions (`PlayerController`, `GameController`)
- Manager: script owning one system's state for the whole run, exposing an API over it, never running a multi-step flow (`AccessoryManager`)
- Coordinator: script running one multi-step flow across several systems, in order (`LevelTransitionCoordinator`)
- Director: script playing one authored timeline, firing content at scripted moments (`WaveDirector`)
- Spawner: script deciding where and when instances enter the scene, leaving construction to a Factory (`EnemySpawner`)

Entity Behaviour:

- Motor: script turning a wanted direction or speed into velocity or force on one body (`CharacterMotor`)
- Sensor: script detecting what surrounds one entity and reporting it, deciding nothing (`VisionSensor`)
- Ability: script for one activatable action of a character, with its own trigger, cost, and cooldown (`DashAbility`)
- Command: script reifying one action as an object, so it can be queued, replayed, or undone (`MoveCommand`)
- State: script holding the behaviour of one state machine node (`PatrolState`)
- StateMachine: script owning one entity's states and the transitions between them (`EnemyStateMachine`)
- Feedback: script playing one burst of particles, sound, or camera shake on request (`HitFeedback`)

Event Delivery:

- Relay: script passing one object's trigger or event callbacks on to an owner, holding no response logic (`DetectionZoneRelay`)
- Channel: SO script acting as one event pipe, so raiser and listener never reference each other (`GameOverEventChannel`)

Event Reaction:

- Listener: script subscribing to one event source, a channel or a subject's C# event, and reacting on its own object (`PauseListener`)
- Binder: script mirroring every state change of one known subject into its own object (`HealthBinder`)

Object Supply:

- Factory: script creating and configuring new instances of one type, hiding how (`EnemyFactory`)
- Pool: script lending and reclaiming reusable instances of one prefab, instead of instantiate and destroy (`BulletPool`)
- Registry: script tracking live instances of one type, which register themselves, for lookup and iteration (`EnemyRegistry`)
- Generator: script producing procedural content from rules and a seed (`LevelGenerator`)
- Provider: script handing out one value or dependency on request, without owning its lifecycle (`InputProvider`)
- Service: plain script behind an interface, with no scene presence and little or no state (`SaveService`)
- Loader: script bringing assets or scenes into memory, usually asynchronously (`SceneLoader`)

User Interface:

- Screen: script on the top object of one full-screen interface, opening, closing, and owning its panels (`PauseScreen`)
- Panel: script for one self-contained region of a screen (`InventoryPanel`)
- Popup: script for a modal prompt shown over the current screen, then dismissed (`ConfirmPopup`)
- Toast: script for a timed, non-modal message shown over play, fading on its own, never blocking input (`HintToast`)
- Widget: script for a small reusable control with its own look and behaviour (`HealthBarWidget`)

World Object:

- Pickup: script for one collectible, handing its reward over once on touch (`BananaPickup`)
- Projectile: script for one thrown or fired thing, flying until it hits or expires (`CoconutProjectile`)
- Zone: script for one volume applying an effect to whatever is inside it (`SlowZone`)

MVP:

- Model: script holding one feature's data and rules, ignorant of any display, raising events on change (`InventoryModel`)
- View: script displaying passively, deciding nothing, exposing what to show and which input occurred (`InventoryView`); without a Presenter, use Panel or Widget
- Presenter: script linking one Model to one View, so neither knows the other (`InventoryPresenter`)

Authored Data:

- Config: SO script holding tunable values, read by whatever it configures (`AudioConfig`)
- Definition: SO script holding authored content of one thing, read-only at runtime (`WeaponDefinition`)
- Setting: SO script holding options the player or project chooses, apart from Config's designer tuning (`GraphicsSetting`)
- Catalog: SO script collecting every Definition of one kind for lookup by id (`ItemCatalog`)
- Preset: script bundling named values, applied in one step (`DifficultyPreset`)
- Save: plain serializable script recording progress, persisted to disk (`PlayerSave`)



#### owner-driven activation pattern

Save a GameObject inactive when it lives for only a stretch of the run; let an owner call `SetActive`, with no `Update` flag guards

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

- hold each target in a `[SerializeField]` reference on the owner, never find it by search
- subscribe and reset in `OnEnable`, unsubscribe in `OnDisable`
- give each target one entry point (`Show`, `Hide`), and call only that from the owner
- assign each toggled group exactly one owner
- toggle component `enabled`, a child visual, or `CanvasGroup` instead when the object must stay findable or listening
- play a hide state before `SetActive(false)` when the object needs an exit animation



#### game tuning

Prefer tunable gameplay numbers in data over code (speed, damage, cooldown, spawn rate, ramp): a designer can then adjust them in the Inspector, even in Play mode, without a recompile. A structural constant (a tag, a layer, an array size) is not tuning, and a `const` suits it.

Tuning leans on three objects, each per its [Class Naming](#class-naming) role:

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

#### tuning with AnimationCurve

Reach for an `AnimationCurve` extensively when a value depends on another value, in place of a formula or a table of constants: difficulty ramping, falloff by distance, damage by charge, speed by health fraction, reward by streak. The designer draws the curve, so its shape can change without code.

Common x axes:

- elapsed time of a run or an encounter
- difficulty level or wave number
- normalized progress, 0~1
- distance, health fraction, stack count

Preferences:

- name the field `<Value>Curve` and state both axes with units in its `[Tooltip]`, x first (`x: ramp progress 0~1; y: spawn interval; s`)
- normalize x to 0~1 when its range varies, and keep the range in a separate Config field (a ramp duration), so one curve serves any length
- hide `Evaluate` behind a Config method that clamps x (`GetInterval(elapsed)`), so a reader need not touch the curve
- give a curve a non-empty initializer (`AnimationCurve.Linear`), since an unset curve evaluates to 0 and silently zeroes the value
- let the y axis be a multiplier on a base value when one curve shapes several values, and absolute when it shapes one
- a plain float still suits a value that depends on nothing

```csharp
[CreateAssetMenu(menuName = "Scriptable Objects/SpawnBalanceConfig")]
public class SpawnBalanceConfig: ScriptableObject {
    // Public Members  #########################################################
    public float GetInterval(float elapsed) =>
        intervalCurve.Evaluate(Mathf.Clamp01(elapsed / rampDuration));

    // Inspector Fields  #######################################################
    [SerializeField]
    [Tooltip("time to full difficulty; s")]
    [Min(0.01f)]
    private float rampDuration = 120f;

    [SerializeField]
    [Tooltip("x: ramp progress 0~1; y: spawn interval; s")]
    private AnimationCurve intervalCurve =
        AnimationCurve.Linear(0f, 2f, 1f, 0.5f);
}
```



#### Logging

Log every meaningful state change so a debug session reads as a sequence of events: lifecycle transitions, branch decisions, external calls (network, save/load, scene loads).

Open every message with the owning subsystem or module name, a colon, and a tab.

Warning and error are reserved for a failed guard clause. Every other log is debug level, gated by `Debug.isDebugBuild` and braced even for one statement.

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





## {description}

Writes, edits & reviews all Unity 6 C# code under house conventions: class-role suffixes, singleton & event idioms, member order, subsystem-prefixed logging

## {when_to_use}

Any C# in a Unity project, even when user never says "Unity": gameplay systems, managers, controllers, editor tools, UI, input, save/load, scene logic. Triggers: Unity, `UnityEngine`, `Debug.Log`, `.cs` under `Assets/`, singleton, manager, event. Load together w/ `u3d-mb` for `MonoBehaviour` scripts, `u3d-so` for `ScriptableObject` classes; asset placement & naming belong to `u3d-assets-management`

## {globs}

```glob
**/*.cs
```

## {[Claude:Skill] Usage}

Invoke `coder` skill via `Skill` tool.

## {[Hermes:skill_view] Usage}

Load `coder` skill with `skill_view`.













## Assets Management

Everything authored lives under one underscore-prefixed root named for the game, `Assets/_MyGame/`, sorting above Unity's own and vendor folders. Paths below are relative to it, and that prefix repeats on any folder that should lead its listing.

```
Assets/_MyGame/Scripts/MinigameRacing/RacingSceneRoot.cs
Assets/_MyGame/Textures/MinigameRacing/StartFlag.png
```



#### Type Folders

One level under the root:

- `Scripts/`: C#
- `Audio/`: music and effects, split above the module level

  - `Audio/BGM/`: module subfolders (eg `Audio/BGM/Lv1/`)
  - `Audio/SFX/`: module subfolders, or category subfolders for effects spanning every module (eg `Audio/SFX/PlayerHit/`)

- `Sprites/`, `Textures/`: 2D art, where split: `Sprites/` gameplay-facing, `Textures/` the rest
- `Animations/`: `.anim` clips, `.controller` graphs
- `Prefabs/`: prefabs
- `Scenes/`: `.unity` files, optionally grouped by area (`Scenes/Minigames/`)
- `Materials/`, `Tilemaps/`: 2D and tilemap work
- `Settings/`: project-level `.asset` files
- `Localizations/`: locale and string-table assets
- `Shaders/`: `.shader`, `.shadergraph`, `.hlsl` files
- `Fonts/`: font files and their `.asset` font settings
- `Input/`: `.inputactions` assets
- `VFX/`: particle systems and Visual Effect Graph assets
- `Timelines/`: `.playable` Timeline assets



#### Module Folders

One short [Pascal Case](#letter-case-pascal-case) name per scene/subsystem, reused identically in every type folder holding its assets: the module name is the constant, the type folder changes around it. Spell it out, never abbreviate. Where modules form a family, the family word leads so the family sorts together:

- Family Member: `MinigameRacing`, `MinigameHiking`, `MinigameHideNSeek`
- Level: `Lv1`, `Lv2`, numbered rather than named
- Screen: `StartScreen`, `PauseScreen`, `SettingsScreen`, every full-screen interface taking the word `Screen`
- Standalone Module: `SaveSystem`, `Inventory`, sharing a name with nothing else
- `_Shared/`: the module slot taken by whatever no single module owns, sorting first on its underscore prefix



#### Asset File Naming

Keep external art, raw downloads, and DAW exports under the filenames they arrived with.

[Pascal Case](#letter-case-pascal-case) throughout, no spaces, no punctuation but the underscore, which carries two jobs and no others:

- Leading: marks a hub, main, or otherwise important asset, sorting it first (`_LevelSelectScene.unity`)
- Inside: separates semantic fields, Pascal Case within each (`Hero_Attack_01`)

Sorting:

- subject first, variant after (`HeroIdle`, `HeroRun`, never `IdleHero`)
- zero-pad every number (`Explosion_02`, `Explosion_10`)
- a texture map carries its channel suffix (`_Albedo`, `_Normal`), a packed map named for the channels it holds (`_MRA`)

By type:

- Scripts: strictly the class the file declares, suffix per [Class Naming](#class-naming) (`PlayerManager.cs` holds `PlayerManager`)
- Scenes: `TitleScene.unity`
- Prefabs: generic name, since the module folder already gives context (`Ball.prefab`)
- Animator controllers: named for the character/object driven (`PlayerAnimator.controller`)
- Animation clips: `Player_Idle.anim`
- Sprites/textures you author: `HealthPotion.png`
- Materials: named for what it is applied to (`Rock.mat`)
- Audio tracks: named for the module or level scored (`RacingBGM.mp3`)
- Audio effects: named for the action it plays on (`ButtonClick.mp3`)
- ScriptableObject/`.asset` instances: prefixed with what they configure (`Lv1LevelConfig.asset`)



### {description}

Places & names Unity project assets & folders across the `Assets/` tree

### {when_to_use}

Creating, moving, renaming, importing any Unity asset, even when user never mentions folder or name: new script file, scene, prefab, audio clip, texture, sprite, animation, material, `.asset` instance. Triggers: "where does this go", "what to name this", "new scene", "import this", folder layout, project structure, `Assets/`. Not for code inside scripts












## MonoBehaviour

Section order, formatting, and accessors follow the example exactly.

Inspector Assignment Guard:

- guard **every** `[SerializeField] private` field carrying no declaration default (`private string label = "default";` needs none)
- **one block, at the top** of `Awake()`, under exactly one `// Inspector Assignment Guard` line, never scattered, never repeated

Inspector Fields:

- prefer `[Tooltip]` on each field, worded per [Briefness Style](#style-briefness-style), and `[Header]` dividing them into groups

```csharp
public class PlayerController: MonoBehaviour {
    // Public Members  #########################################################
    public GameState currentState;

    // Public Methods  #########################################################
    public static PlayerController FindInScene() { ... }

    // Inspector Fields  #######################################################
    [SerializeField]
    [Tooltip("scene to load on race end")]
    private string nextSceneName;

    [Header("Movement")]
    [SerializeField]
    [Tooltip("top speed; u/s")]
    private float maxSpeed = 5f;

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
    private float acceleration;

    // cached references  ------------------------------------------------------
    private Rigidbody2D body;

    // private methods  ########################################################
    private void PlayIntroSequence() { ... }
}
```



### {description}

Writes & edits Unity `MonoBehaviour` scripts: components attached to GameObjects, w/ fixed section layout & Inspector field guards

### {when_to_use}

Any Unity script attached to a GameObject, the default shape of most gameplay code, even when user never names `MonoBehaviour`: player, enemy, spawner, trigger zone, camera rig, UI behaviour. Triggers: `MonoBehaviour`, `[SerializeField]`, `Awake`, `Start`, `Update`, `OnTriggerEnter`, `GetComponent`, Inspector field, "add a component", "attach to GameObject". Apply alongside `u3d`, never in place of it. Not for plain C# classes, `ScriptableObject`, asset placement













## Scriptable Object

### {description}

Writes & edits Unity `ScriptableObject` classes & their `.asset` data instances

### {when_to_use}

Any designer-editable data living outside a scene, even when user only says "config", "settings", "database", "shared data": level configs, item & enemy stats, tuning tables, event channels. Triggers: `ScriptableObject`, `CreateAssetMenu`, `CreateInstance`, `.asset`, data container. Apply alongside `u3d`. Not for `MonoBehaviour` components, plain `[Serializable]` classes, asset placement
