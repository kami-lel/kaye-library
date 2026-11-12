# kaye-library: Blueprint Documentation

How the library's blueprints connect; the rest is a command away: `kaye-library blueprint list`, `blueprint show NAME`, `blueprint preview NAME`, `exportable ls`. A blueprint name is contract for [consumers](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md). Rules for changing one are in [AGENTS.md](../AGENTS.md), the architecture in [CONTEXT.md](../CONTEXT.md), the overview in the [README](../README.md).

## Blueprint Dependency Graph

Every `dependencies=[...]` edge a library blueprint declares; `A --> B` reads "A depends on B".

#### Agentic & Coder

```mermaid
flowchart LR
    halt_each_movement["halt-each-movement"] --> agent_movement_and_suite["agent-movement-and-suite"]
    cascade_all_movements["cascade-all-movements"] --> agent_movement_and_suite
    plan_for_suite["plan-for-suite"] --> agent_movement_and_suite
    plan_for_suite_execution["plan-for-suite-execution"] --> agent_movement_and_suite
    sync_unit_test["sync-unit-test"] --> agent_movement_and_suite_with_count["agent-movement-and-suite-with-count"]
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
    equip_proj_for_agent["equip-proj-for-agent"] --> proj_context_engineering["proj-context-engineering"]
    repo_readme_writer["repo-readme-writer"] --> style_briefness_style["style-briefness-style"]
    repo_changelog_writer["repo-changelog-writer"] --> style_briefness_style
    repo_changelog_writer --> proj_version_extended["proj-version-extended"]
    repo_changelog_writer --> style_good_writing
    ready_release_version["ready-release-version"] --> proj_version_extended
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
    commit_sense_branch_merging --> git_feature_summary["git-feature-summary"]
    commit_sense_branch_merging --> proj_version_title["proj-version-title"]
    git_sense_dify_primary["git-sense-dify-primary"] --> git_sense_primary_summary
    git_sense_dify_per_file["git-sense-dify-per-file"] --> git_sense_per_file_change_sigil
    git_sense_dify_per_file --> git_sense_per_file_summary
    git_feature_summary["git-feature-summary"] --> git_feature_discover["git-feature-discover"]
    ready_land_feature["ready-land-feature"] --> git_feature_discover
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
    scan_event_radar_daily["scan-event-radar-daily"] --> secretary_event_brief_format
    scan_event_radar_weekly["scan-event-radar-weekly"] --> secretary_event_brief_format
    scan_event_radar_daily --> agent_unreachable_task_workaround["agent-unreachable-task-workaround"]
    scan_event_radar_weekly --> agent_unreachable_task_workaround
    hunt_job_opportunity["hunt-job-opportunity"] --> agent_unreachable_task_workaround
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

#### Standalone Chat

```mermaid
flowchart LR
    chat --> style_markdown["style-markdown"]
    chat --> element_alphabetical_sequence_numbering_in_chat["element-alphabetical-sequence-numbering-in-chat"]
    element_alphabetical_sequence_numbering_in_chat --> element_alphabetical_sequence_numbering["element-alphabetical-sequence-numbering"]
    chat_coder["chat-coder"] --> chat
    chat_coder --> coder
    rapid --> style_markdown
```

## Blueprint Invocation Graph

Every `Invoke ... skill via Skill tool` call; `A --> B` reads "A invokes B" at runtime.

```mermaid
flowchart LR
    coder_profiles["coder-* language profiles"] --> coder
    coder_ue["coder-ue"] --> coder_c["coder-c"]
    coder --> sync_unit_test["sync-unit-test"]
    coder --> plan_for_suite_execution["plan-for-suite-execution"]
    coder --> cascade_all_movements["cascade-all-movements"]
    coder --> halt_each_movement["halt-each-movement"]
    working_with_git["working-with-git"] --> commit_sense["commit-sense"]
    good_morning["good-morning"] --> sweep_email_inbox["sweep-email-inbox"]
    good_morning --> recap_yesterday["recap-yesterday"]
    good_morning --> scan_event_radar_daily["scan-event-radar-daily"]
    good_morning --> hunt_job_opportunity["hunt-job-opportunity"]
    good_week["good-week"] --> scan_event_radar_weekly["scan-event-radar-weekly"]
    good_week --> hunt_job_opportunity
```
