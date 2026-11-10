# Unity Engine

Follows [Coder C Sharp](#coder-c-sharp)

Writing code based on [Coder](#coder)

Decode-only, never output the shorthand:

(((u3d-abbr)))

When naming an identifier, always use shorthand below over full word; decode any user writes:

(((u3d-identifier)))





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


































## Naming

One convention names every noun-type thing: class, member, variable, file, GameObject, folder.

- Casing: code per [Coder](#coder); asset file, folder, and GameObject in [Pascal Case](#letter-case-pascal-case)
- Characters: no spaces or punctuation but the underscore, per [Underscore Usage](#underscore-usage)
- Order: subject first, qualifier after, so related names sort together (`HeroIdle`, `HeroRun`, never `IdleHero`)
- Subject: name what a thing is or serves, omitting what its folder already says (`Ball.prefab`, `Rock.mat`, `ButtonClick.mp3`)
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
- Variant or State: an inner `_` splits the subject from what tells one version of it apart, Pascal Case within each field (`Banana_Ripe.mat`, `Banana_Raw.mat`, `Player_Idle.anim`); use it whenever several things differ only by variant or state, such as two materials of one object, a sprite per state, or a prefab variant (`Popup_Confirm`, beside `_PopupBase`); a further field may follow, such as a frame number or action (`Hero_Attack_01`)
- Channel: a texture map takes its channel as the variant field (`_Albedo`, `_Normal`), a packed map named for the channels it holds (`_MRA`)


































## Common Type and Suffix

Each type names a concept, not a script: give its suffix to whatever embodies that concept, be it a class, script or asset file, GameObject, prefab, or variable.

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

User Interface:

- Screen: one full-screen interface, opening, closing, and owning its panels (`PauseScreen`)
- Panel: one self-contained region of a screen (`InventoryPanel`)
- Popup: a modal prompt shown over the current screen, then dismissed (`ConfirmPopup`)
- Toast: a timed, non-modal message shown over play, fading on its own, never blocking input (`HintToast`)
- Widget: a small reusable control with its own look and behaviour (`HealthBarWidget`)

MVP:

- Model: one feature's data and rules, ignorant of any display, raising events on change (`InventoryModel`)
- View: a passive display deciding nothing, exposing what to show and which input occurred (`InventoryView`); without a Presenter, use Panel or Widget
- Presenter: links one Model to one View, so neither knows the other (`InventoryPresenter`)

Authored Data:

- Config: tunable values, read by whatever it configures (`AudioConfig`)
- Definition: the authored content of one thing, read-only at runtime (`WeaponDefinition`)
- Setting: options the player or project chooses, apart from a Config's designer tuning (`GraphicsSetting`)
- Catalog: every Definition of one kind, collected for lookup by id (`ItemCatalog`)
- Preset: named values bundled to apply in one step (`DifficultyPreset`)
- Save: a record of progress, persisted to disk (`PlayerSave`)


































## Coding

- `var` only for a `foreach` local or a long generic right-hand side
- singleton: expose the instance through a static member named exactly `I` (`GamepadManager.I`)
- events: prefer the C# `event` keyword over `UnityEvent` (`public event Action<int> HealthChanged;`)
- member order in a plain class: `[SerializeField]` fields, public API, plain fields, private helpers, constructor last; a `MonoBehaviour` follows its own example below
- banners per [Comment Banner](#comment-banner), laid out as the example shows, and none at all in a small or single-purpose file
- name every class, member, and variable per [Naming](#naming), suffixed per [Common Type and Suffix](#common-type-and-suffix) and [Unit Usage](#unit-usage)



#### Input

Read gameplay input through the Input System: `InputAction`s from an Input Actions asset, never a keyboard, mouse, or gamepad directly. Express timing, such as a double-tap, as an interaction (`MultiTap`), never as a hand-rolled key tracker



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













### Inspector Field

- declare as `[SerializeField] private`, never a public field
- prefer `[Tooltip]` on each field, worded in briefness style, ending with its unit
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













### MonoBehaviour

Section order, formatting, and accessors follow the example exactly.

Inspector Assignment Guard:

- guard **every** `[SerializeField] private` field carrying no declaration default (`private string label = "default";` needs none)
- **one block, at the top** of `Awake()`, under exactly one `// Inspector Assignment Guard` line, never scattered, never repeated

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













### Scriptable Object

Section order, formatting, and accessors follow the example exactly.

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































## Assets Management

Everything authored lives under one underscore-prefixed root named for the game, `Assets/_MyGame/`, sorting above Unity's own and vendor folders. Paths below are relative to it, and that prefix repeats on any folder that should lead its listing.

```
Assets/_MyGame/Scripts/MinigameRacing/RacingSceneRoot.cs
Assets/_MyGame/Textures/MinigameRacing/StartFlag.png
```

Name every asset file, folder, and GameObject per [Naming](#naming).





#### Folders

Type folders, one level under the root:

- `Scripts/`: C#
- `Audio/`: music and effects, split above the module level, per the audio subfolders below
- `Sprites/`, `Textures/`: 2D art, where split: `Sprites/` gameplay-facing, `Textures/` the rest
- `Animations/`: `.anim` clips, `.controller` graphs
- `Prefabs/`: prefabs
- `Scenes/`: `.unity` files, optionally grouped by area (`Scenes/Minigames/`)
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

Audio subfolders:

- `Audio/BGM/`: module subfolders (eg `Audio/BGM/Lv1/`)
- `Audio/SFX/`: module subfolders, or category subfolders for effects spanning every module (eg `Audio/SFX/PlayerHit/`)

Module folders: one short [Pascal Case](#letter-case-pascal-case) name per scene/subsystem, reused identically in every type folder holding its assets: the module name is the constant, the type folder changes around it. Spell it out, never abbreviate. Where modules form a family, the family word leads so the family sorts together:

- Family Member: `MinigameRacing`, `MinigameHiking`, `MinigameHideNSeek`
- Level: `Lv1`, `Lv2`, numbered rather than named
- Screen: `StartScreen`, `PauseScreen`, `SettingsScreen`, every full-screen interface taking the word `Screen`
- Standalone Module: `SaveSystem`, `Inventory`, sharing a name with nothing else
- `_Shared/`: the module slot taken by whatever no single module owns, sorting first on its underscore prefix



































## Prefab Usage

Reach for prefabs extensively: turn an object into a prefab as soon as a reason below holds, progressively as the project grows, rather than waiting for a cleanup pass.

Make a prefab when:

- 2 or more objects are copies or variants of each other
- the object could be reused elsewhere, such as in another scene, even if it is used once today

Prefer the base and variant pattern for a family of near-identical objects:

- base prefab: holds everything the family shares, named with a leading `_`, the subject, and `Base` (`_PopupBase.prefab`)
- variant prefab: a Prefab Variant of the base, overriding only what differs, named per [Underscore Usage](#underscore-usage) (`Popup_Confirm.prefab`)
- put a change shared by the whole family in the base, so every variant follows it
- a scene holds instances of the prefab, never a hand-made copy of one


































## Owner-Driven Activation

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
- rest each object in its original active state: a screen is saved inactive and switched on by its owner, a manager is saved active and stays so
- toggle component `enabled`, a child visual, or `CanvasGroup` instead when the object must stay findable or listening
- play a hide state before `SetActive(false)` when the object needs an exit animation

























## Game Tuning

Prefer tunable gameplay numbers in data over code (speed, damage, cooldown, spawn rate, ramp): a designer can then adjust them in the Inspector, even in Play mode, without a recompile. A structural constant (a tag, a layer, an array size) is not tuning, and a `const` suits it.

Tuning leans on three objects, each per its [Common Type and Suffix](#common-type-and-suffix) role:

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

- name the field `<Value>Curve` and state both axes with units in its `[Tooltip]`, x first (`x: ramp progress 0~1; y: spawn interval; s`)
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
