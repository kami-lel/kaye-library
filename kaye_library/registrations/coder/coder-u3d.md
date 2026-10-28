## Coder Unity Engine

Follows [Coder C Sharp](#coder-c-sharp)

Writing code based on [Coder](#coder)

Decode-only, never output the shorthand:

(((coder-u3d-abbr)))

When naming an identifier, always use shorthand below over full word; decode any user writes:

(((coder-u3d-identifier)))



##### coding for unity engine

- `var` only for a `foreach` local or a long generic right-hand side
- singleton: expose the instance through a static member named exactly `I` (`GamepadManager.I`)
- events: prefer the C# `event` keyword over `UnityEvent` (`public event Action<int> HealthChanged;`)
- member order in a plain class: `[SerializeField]` fields, public API, plain fields, private helpers, constructor last; a `MonoBehaviour` follows its own example below
- banners per [Comment Banner](#comment-banner), laid out as the example shows, and none at all in a small or single-purpose file



##### class naming

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

- Listener: script subscribing to one event channel and reacting on its own object (`PauseListener`)
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
- Widget: script for a small reusable control with its own look and behaviour (`HealthBarWidget`)

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



##### owner-driven activation pattern

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



##### Logging

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





### {description}

Writes, edits & reviews all Unity 6 C# code under house conventions: class-role suffixes, singleton & event idioms, member order, subsystem-prefixed logging

### {when_to_use}

Any C# in a Unity project, even when user never says "Unity": gameplay systems, managers, controllers, editor tools, UI, input, save/load, scene logic. Triggers: Unity, `UnityEngine`, `Debug.Log`, `.cs` under `Assets/`, singleton, manager, event. Load together w/ `coder-u3d-mb` for `MonoBehaviour` scripts, `coder-u3d-so` for `ScriptableObject` classes; asset placement & naming belong to `coder-u3d-assets-management`

### {globs}

```glob
**/*.cs
```

### {[ClaudeCode:Skill] Usage}

Invoke `coder` skill via `Skill` tool.













### Assets Management

Everything authored lives under one underscore-prefixed root named for the game, `Assets/_MyGame/`, sorting above Unity's own and vendor folders. Paths below are relative to it, and that prefix repeats on any folder that should lead its listing.

```
Assets/_MyGame/Scripts/MinigameRacing/RacingSceneRoot.cs
Assets/_MyGame/Textures/MinigameRacing/StartFlag.png
```



##### Type Folders

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



##### Module Folders

One short [Pascal Case](#letter-case-pascal-case) name per scene/subsystem, reused identically in every type folder holding its assets: the module name is the constant, the type folder changes around it. Spell it out, never abbreviate. Where modules form a family, the family word leads so the family sorts together:

- Family Member: `MinigameRacing`, `MinigameHiking`, `MinigameHideNSeek`
- Level: `Lv1`, `Lv2`, numbered rather than named
- Screen: `StartScreen`, `PauseScreen`, `SettingsScreen`, every full-screen interface taking the word `Screen`
- Standalone Module: `SaveSystem`, `Inventory`, sharing a name with nothing else
- `_Shared/`: the module slot taken by whatever no single module owns, sorting first on its underscore prefix



##### Asset File Naming

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



#### {description}

Places & names Unity project assets & folders across the `Assets/` tree

#### {when_to_use}

Creating, moving, renaming, importing any Unity asset, even when user never mentions folder or name: new script file, scene, prefab, audio clip, texture, sprite, animation, material, `.asset` instance. Triggers: "where does this go", "what to name this", "new scene", "import this", folder layout, project structure, `Assets/`. Not for code inside scripts












### MonoBehaviour

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



#### {description}

Writes & edits Unity `MonoBehaviour` scripts: components attached to GameObjects, w/ fixed section layout & Inspector field guards

#### {when_to_use}

Any Unity script attached to a GameObject, the default shape of most gameplay code, even when user never names `MonoBehaviour`: player, enemy, spawner, trigger zone, camera rig, UI behaviour. Triggers: `MonoBehaviour`, `[SerializeField]`, `Awake`, `Start`, `Update`, `OnTriggerEnter`, `GetComponent`, Inspector field, "add a component", "attach to GameObject". Apply alongside `coder-u3d`, never in place of it. Not for plain C# classes, `ScriptableObject`, asset placement













### Scriptable Object

#### {description}

Writes & edits Unity `ScriptableObject` classes & their `.asset` data instances

#### {when_to_use}

Any designer-editable data living outside a scene, even when user only says "config", "settings", "database", "shared data": level configs, item & enemy stats, tuning tables, event channels. Triggers: `ScriptableObject`, `CreateAssetMenu`, `CreateInstance`, `.asset`, data container. Apply alongside `coder-u3d`. Not for `MonoBehaviour` components, plain `[Serializable]` classes, asset placement
