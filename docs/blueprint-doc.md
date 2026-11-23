# Kaye Library: Blueprint Documentation

How the library's blueprints connect; the rest is a command away: `kaye-library blueprint list`, `blueprint show NAME`, `blueprint preview NAME`, `exportable ls`. A blueprint name is contract for [consumers](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md). Rules for changing one are in [AGENTS.md](../AGENTS.md), the architecture in [CONTEXT.md](../CONTEXT.md), the overview in the [README](../README.md).

## Blueprint Dependency Graph

Every `dependencies=[...]` edge a library blueprint declares; `A --> B` reads "A depends on B".

#### Agentic & Coder

```mermaid
flowchart LR
    halt_each_movement["halt-each-movement"] --> agent_movement_and_suite["agent-movement-and-suite"]
    cascade_all_movements["cascade-all-movements"] --> agent_movement_and_suite
    plan_for_suite["plan-for-suite"] --> agent_movement_and_suite
    execute_plan_for_suite["execute-plan-for-suite"] --> agent_movement_and_suite
    rework_plan_for_suite["rework-plan-for-suite"] --> agent_movement_and_suite
    sync_unit_test["sync-unit-test"] --> agent_movement_and_suite_with_count["agent-movement-and-suite-with-count"]
    plan_for_suite --> agent_files_and_folders["agent-files-and-folders"]
    agent_files_and_folders --> style_letter_case_kebab_case["style-letter-case-kebab-case"]
    agent_files_and_folders --> style_letter_case_pascal_case["style-letter-case-pascal-case"]
    agent_files_and_folders --> element_dt_year_month_day_format["element-dt-year-month-day-format"]
    sync_unit_test --> element_triage_tags["element-triage-tags"]
    review_gaps["review-gaps"] --> element_triage_tags
    coder --> element_triage_tags
    coder --> repo_structure["repo-structure"]
    coder --> proj_context_engineering["proj-context-engineering"]
    coder --> style_briefness_style["style-briefness-style"]
    coder --> style_letter_case_snake_case["style-letter-case-snake-case"]
    coder --> style_letter_case_all_caps["style-letter-case-all-caps"]
    coder_command_usage_message["coder-command-usage-message"] --> style_letter_case_all_caps
    coder_cpp["coder-cpp"] --> coder_c["coder-c"]
    coder_ue["coder-ue"] --> coder_cpp
    u3d --> coder_c_sharp["coder-c-sharp"]
    u3d_coding["u3d-coding"] --> coder_c_sharp
    u3d_mb["u3d-mb"] --> style_briefness_style
```

#### Repository & Project

```mermaid
flowchart LR
    proj_agents_writer["proj-agents-writer"] --> proj_agents["proj-agents"]
    repo_agents_writer["repo-agents-writer"] --> proj_agents
    proj_doc_writer["proj-doc-writer"] --> proj_docs["proj-docs"]
    repo_doc_writer["repo-doc-writer"] --> proj_docs
    proj_doc_writer --> style_good_writing["style-good-writing"]
    repo_doc_writer --> style_good_writing
    proj_doc_writer --> element_secondary_language_marking["element-secondary-language-marking"]
    repo_doc_writer --> element_secondary_language_marking
    proj_doc_writer --> agent_files_and_folders["agent-files-and-folders"]
    repo_doc_writer --> agent_files_and_folders
    equip_proj_for_agent["equip-proj-for-agent"] --> proj_context_engineering["proj-context-engineering"]
    repo_readme_writer["repo-readme-writer"] --> style_briefness_style["style-briefness-style"]
    repo_readme_writer --> element_secondary_language_marking
    repo_changelog_writer["repo-changelog-writer"] --> style_briefness_style
    repo_changelog_writer --> proj_version_extended["proj-version-extended"]
    repo_changelog_writer --> style_good_writing
    repo_credits_writer["repo-credits-writer"] --> style_briefness_style
    repo_credits_writer --> style_good_writing
    repo_devlog_writer["repo-devlog-writer"] --> style_briefness_style
    repo_devlog_writer --> style_good_writing
    repo_devlog_writer --> element_dt_year_month_day_format["element-dt-year-month-day-format"]
    repo_devlog_writer --> proj_version_title
    repo_devlog_writer --> style_markdown_file_assets["style-markdown-file-assets"]
    repo_devlog_writer --> element_triage_tags["element-triage-tags"]
    ready_release_version["ready-release-version"] --> proj_version_extended
    scrub_released_version["scrub-released-version"] --> proj_version_title["proj-version-title"]
    ready_release_version --> agent_movement_and_suite["agent-movement-and-suite"]
    scrub_released_version --> agent_movement_and_suite
    release_version["release-version"] --> agent_movement_and_suite
    proj_version_title["proj-version-title"] --> proj_version_bump["proj-version-bump"]
    proj_version_bump --> proj_version["proj-version"]
    proj_version_extended --> proj_version
    initialize_repo["initialize-repo"] --> style_good_writing
    maintenance_before_compact["maintenance-before-compact"] --> style_good_writing
    condense_agents_and_context["condense-agents-and-context"] --> repo_agents_writer
    condense_agents_and_context --> repo_context_writer["repo-context-writer"]
    create_project_agents["create-project-agents"] --> proj_agents_writer
    maintain_project_agents["maintain-project-agents"] --> proj_agents_writer
    create_project_docs["create-project-docs"] --> proj_doc_writer
    maintain_project_docs["maintain-project-docs"] --> proj_doc_writer
    create_readme["create-readme"] --> repo_readme_writer
    maintain_readme["maintain-readme"] --> repo_readme_writer
    create_readme --> style_good_writing
    maintain_readme --> style_good_writing
    create_changelog["create-changelog"] --> repo_changelog_writer
    maintain_changelog["maintain-changelog"] --> repo_changelog_writer
    condense_changelog["condense-changelog"] --> repo_changelog_writer
    create_credits["create-credits"] --> repo_credits_writer
    maintain_credits["maintain-credits"] --> repo_credits_writer
    create_devlog["create-devlog"] --> repo_devlog_writer
    maintain_devlog["maintain-devlog"] --> repo_devlog_writer
    create_credits --> style_good_writing
    maintain_credits --> style_good_writing
    create_devlog --> style_good_writing
    maintain_devlog --> style_good_writing
    create_repo_agents["create-repo-agents"] --> repo_agents_writer
    maintain_repo_agents["maintain-repo-agents"] --> repo_agents_writer
    create_repo_docs["create-repo-docs"] --> repo_doc_writer
    maintain_repo_docs["maintain-repo-docs"] --> repo_doc_writer
```

#### Git

```mermaid
flowchart LR
    commit_sense["commit-sense"] --> git_sense_core["git-sense-core"]
    commit_sense --> git_sense_primary_summary["git-sense-primary-summary"]
    commit_sense --> git_sense_per_file_change_sigil["git-sense-per-file-change-sigil"]
    commit_sense --> git_sense_per_file_summary["git-sense-per-file-summary"]
    git_sense_primary_summary --> git_sense_core
    git_sense_per_file_change_sigil --> git_sense_core
    git_sense_per_file_summary --> git_sense_core
    commit_sense_branch_merging["commit-sense-branch-merging"] --> git_sense_core
    commit_sense_branch_merging --> git_feature_branch["git-feature-branch"]
    commit_sense_branch_merging --> git_hotfix_branch["git-hotfix-branch"]
    commit_sense_branch_merging --> git_release_branch["git-release-branch"]
    commit_sense_branch_merging --> git_feature_summary["git-feature-summary"]
    commit_sense_branch_merging --> proj_version_title["proj-version-title"]
    git_sense_dify_primary["git-sense-dify-primary"] --> git_sense_primary_summary
    git_sense_dify_per_file["git-sense-dify-per-file"] --> git_sense_per_file_change_sigil
    git_sense_dify_per_file --> git_sense_per_file_summary
    git_feature_summary["git-feature-summary"] --> git_feature_discover["git-feature-discover"]
    ready_land_feature["ready-land-feature"] --> git_feature_discover
    scrub_landed_feature["scrub-landed-feature"] --> git_feature_branch
    ready_land_feature --> agent_movement_and_suite["agent-movement-and-suite"]
    scrub_landed_feature --> agent_movement_and_suite
    land_feature["land-feature"] --> agent_movement_and_suite
    submit_pr["submit-pr"] --> ready_land_feature
    submit_pr --> git_feature_summary
    tend_linked_wt["tend-linked-wt"] --> plant_linked_wt["plant-linked-wt"]
    tend_linked_wt --> uproot_linked_wt["uproot-linked-wt"]
    plant_linked_wt --> tend_linked_wt_core["tend-linked-wt-core"]
    uproot_linked_wt --> tend_linked_wt_core
    git_feature_summary --> style_briefness_style["style-briefness-style"]
    git_feature_summary --> style_letter_case_commentary_case["style-letter-case-commentary-case"]
```

#### Meta Prompt & Amanuensis

```mermaid
flowchart LR
    write_llm_prompt["write-llm-prompt"] --> meta_prompt["meta-prompt"]
    write_for_skill["write-for-skill"] --> meta_prompt
    write_skill_description["write-skill-description"] --> write_for_skill
    write_skill_when_to_use["write-skill-when-to-use"] --> write_for_skill
    write_skill_description_and_when_to_use["write-skill-description-and-when-to-use"] --> write_skill_description
    write_skill_description_and_when_to_use --> write_skill_when_to_use
    amanuensis_chicago_note["amanuensis-chicago-note"] --> style_markdown_footnotes["style-markdown-footnotes"]
    bibliographer --> style_markdown_footnotes
    assemble_bibliography["assemble-bibliography"] --> amanuensis_chicago_bibliography["amanuensis-chicago-bibliography"]
    dispositor --> style_heading_separation["style-heading-separation"]
    dispositor --> style_good_writing["style-good-writing"]
    dispositor --> agent_files_and_folders["agent-files-and-folders"]
    scholiast --> dispositor
    minutes_clerk["minutes-clerk"] --> dispositor
    config_writer["config-writer"] --> dispositor
    config_writer --> style_briefness_style["style-briefness-style"]
    keybinding_writer["keybinding-writer"] --> config_writer
```

#### Secretary

```mermaid
flowchart LR
    field_date_time["secretary-report-info-field-date-time"] --> element_dt_month_day_format["element-dt-month-day-format"]
    field_date_time --> element_dt_time_format["element-dt-time-format"]
    field_deadline["secretary-report-info-field-deadline"] --> element_dt_month_day_format
    field_deadline --> element_dt_time_format
    element_dt_watch_day["element-dt-watch-day"] --> element_dt_time_format
    secretary_event_brief_format["secretary-event-brief-format"] --> style_briefness_style["style-briefness-style"]
    secretary_event_brief_format --> field_date_time
    secretary_event_brief_format --> field_location["...-field-location"]
    secretary_event_brief_format --> field_link["...-field-link"]
    secretary_event_brief_format --> field_ticket["...-field-ticket"]
    sweep_email_inbox["sweep-email-inbox"] --> field_deadline
    sweep_email_inbox --> field_link
    sweep_email_inbox --> field_source["...-field-source"]
    sweep_email_inbox --> agent_movement_and_suite["agent-movement-and-suite"]
    push_event_to_calendar["push-event-to-calendar"] --> agent_movement_and_suite
    push_task_to_gtd["push-task-to-gtd"] --> agent_movement_and_suite
    scan_event_radar_daily["scan-event-radar-daily"] --> secretary_event_brief_format
    scan_event_radar_weekly["scan-event-radar-weekly"] --> secretary_event_brief_format
    scan_event_radar_daily --> agent_task_blockage_workaround["agent-task-blockage-workaround"]
    scan_event_radar_weekly --> agent_task_blockage_workaround
    hunt_job_opportunity["hunt-job-opportunity"] --> agent_task_blockage_workaround
    hunt_job_opportunity --> style_briefness_style
    hunt_job_opportunity --> field_date_time
    hunt_job_opportunity --> field_deadline
    hunt_job_opportunity --> field_location
    hunt_job_opportunity --> field_link
    hunt_job_opportunity --> field_source
    recap_yesterday["recap-yesterday"] --> element_dt_watch_day
    recap_today["recap-today"] --> element_dt_watch_day
    recap_yesterday --> style_briefness_style
    recap_today --> style_briefness_style
```

#### Chat

```mermaid
flowchart LR
    chat_basic["chat-basic"] --> style_markdown["style-markdown"]
    chat_basic --> element_alphabetical_sequence_numbering_in_chat["element-alphabetical-sequence-numbering-in-chat"]
    chat --> chat_basic
    chat_basic_kaye["chat-basic-kaye"] --> chat_basic
    chat_basic_kaye --> persona
    chat_kaye["chat-kaye"] --> chat
    chat_kaye --> persona
    element_alphabetical_sequence_numbering_in_chat --> element_alphabetical_sequence_numbering["element-alphabetical-sequence-numbering"]
    coder --> chat
    coder --> persona
    rapid --> style_markdown
```

## Registration

Every blueprint registers in `kaye_library/registrations/<group>/<group>_bp.py` through the helpers of `registrations/_common.py`: `register_exportable`, `register_prompt`, `register_internal` and `register_abbr_glossary`, bound to the `kaye-library` consumer by the engine's `bind_registrars`, plus the engine's `register_node`, `register_leaf` and `glossary_blueprint`, which `_common.py` re-exports. They are `kaye-engine` public API, so a third consumer builds its own the same way; see the engine's [Registration Helpers](https://github.com/kami-lel/kaye-engine/blob/dev/docs/prompt-doc.md#registration-helpers). A blueprint is built whole before it registers, never edited afterwards.

`chat` and `persona` are internal and persona-free; `chat-kaye`, `chat-basic-kaye` and `coder` stack on them and turn `for Kaye` and `in chat` on, so the entry's render profile picks the persona and the chat format. A consumer replaces `chat` or `persona` in place with `override_blueprint`, so every entry picks up its version by name, and re-homes `chat-kaye` into its plugin with `override_exportable`; `coder` never depends on `chat-kaye`, so what a consumer adds there stays out of `coder`.

## Blueprint Invocation Graph

Every `Invoke ... skill via Skill tool` call a skill's own text makes, dependencies' calls left to them; `A --> B` reads "A invokes B" at runtime.

#### Agentic & Coder

```mermaid
flowchart LR
    coder_profiles["coder-* language profiles"] --> coder
    coder_ue["coder-ue"] --> coder_c["coder-c"]
    coder --> sync_unit_test["sync-unit-test"]
    plan_for_suite["plan-for-suite"] --> execute_plan_for_suite["execute-plan-for-suite"]
    plan_for_suite --> cascade_all_movements["cascade-all-movements"]
    plan_for_suite --> halt_each_movement["halt-each-movement"]
    plan_for_suite --> rework_plan_for_suite["rework-plan-for-suite"]
    plan_for_suite --> tend_linked_wt["tend-linked-wt"]
    plan_for_suite --> commit_sense["commit-sense"]
    execute_plan_for_suite --> cascade_all_movements
    execute_plan_for_suite --> halt_each_movement
    execute_plan_for_suite --> rework_plan_for_suite
    execute_plan_for_suite --> commit_sense
```

#### Git & Repository

```mermaid
flowchart LR
    working_with_git["working-with-git"] --> commit_sense["commit-sense"]
    initialize_repo["initialize-repo"] --> create_readme["create-readme"]
    initialize_repo --> create_changelog["create-changelog"]
    initialize_repo --> create_repo_agents["create-repo-agents"]
    initialize_repo --> create_repo_docs["create-repo-docs"]
    maintenance_before_compact["maintenance-before-compact"] --> maintain_changelog["maintain-changelog"]
    maintenance_before_compact --> maintain_repo_agents["maintain-repo-agents"]
    repo_changelog_writer["repo-changelog-writer"] --> sync_unit_test["sync-unit-test"]
    repo_devlog_writer["repo-devlog-writer"] --> proj_version_title["proj-version-title"]
    equip_proj_for_agent["equip-proj-for-agent"] --> proj_agents_writer["proj-agents-writer"]
    submit_pr["submit-pr"] --> ready_land_feature["ready-land-feature"]
    ready_land_feature --> sync_unit_test
    ready_land_feature --> maintain_changelog
    ready_land_feature --> maintain_repo_agents
    ready_land_feature --> commit_sense
    land_feature["land-feature"] --> ready_land_feature
    land_feature --> commit_sense_branch_merging["commit-sense-branch-merging"]
    land_feature --> resolve_merge_conflict["resolve-merge-conflict"]
    land_feature --> scrub_landed_feature["scrub-landed-feature"]
    scrub_landed_feature --> uproot_linked_wt["uproot-linked-wt"]
    ready_release_version["ready-release-version"] --> maintain_readme["maintain-readme"]
    ready_release_version --> maintain_credits["maintain-credits"]
    ready_release_version --> condense_changelog["condense-changelog"]
    ready_release_version --> condense_agents_and_context["condense-agents-and-context"]
    ready_release_version --> maintain_repo_docs["maintain-repo-docs"]
    release_version["release-version"] --> ready_release_version
    release_version --> commit_sense
    release_version --> commit_sense_branch_merging
    release_version --> resolve_merge_conflict
    release_version --> scrub_released_version["scrub-released-version"]
    scrub_released_version --> prune_merged_branches["prune-merged-branches"]
    scrub_released_version --> commit_sense
```

#### Secretary & Amanuensis

```mermaid
flowchart LR
    good_morning["good-morning"] --> sweep_email_inbox["sweep-email-inbox"]
    good_morning --> recap_yesterday["recap-yesterday"]
    good_morning --> scan_event_radar_daily["scan-event-radar-daily"]
    good_morning --> hunt_job_opportunity["hunt-job-opportunity"]
    good_week["good-week"] --> scan_event_radar_weekly["scan-event-radar-weekly"]
    good_week --> hunt_job_opportunity
    recap_today["recap-today"] --> pull_task_from_gtd["pull-task-from-gtd"]
    recap_yesterday --> pull_task_from_gtd
    bibliographer --> amanuensis_chicago_note["amanuensis-chicago-note"]
```

#### Unity

Each Unity skill may invoke its siblings "if needed"; the entry points are shown, the sibling web is in `u3d.md`.

```mermaid
flowchart LR
    u3d --> u3d_coding["u3d-coding"]
    u3d --> u3d_naming["u3d-naming"]
    u3d --> u3d_assets_management["u3d-assets-management"]
    u3d --> coder_c_sharp["coder-c-sharp"]
    u3d_coding --> coder_comment_banner["coder-comment-banner-in-code-comment"]
    u3d_naming --> coder
    u3d_naming --> style_letter_case_pascal_case["style-letter-case-pascal-case"]
    u3d_assets_management --> style_letter_case_pascal_case
```
