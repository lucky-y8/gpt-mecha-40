# Third-party provenance and acknowledgements

This project references, but does not claim authorship of, the following upstream projects.

## Open Duck Mini

- Repository: https://github.com/apirrone/Open_Duck_Mini
- Reference branch: v2
- Audited commit: b23317a485b3cec7d8417f352478778b3475173c
- Upstream license: Apache License 2.0 (see upstream LICENSE file)
- Role: mechanical reference, print files, assembly documentation and project hub.

## Open Duck Mini Runtime

- Repository: https://github.com/apirrone/Open_Duck_Mini_Runtime
- Reference branch: v2
- Audited commit: 376de65435c93486347cd601a31aa96951799896
- Role: embedded runtime and actuator/policy execution reference.
- License status: no root LICENSE/COPYING/NOTICE file was present in the inspected v2 repository tree. Do not copy or modify its source files into this repository until the authors' licensing terms are confirmed. Linking to the upstream repository is fine.

## Open Duck Playground

- Repository: https://github.com/apirrone/Open_Duck_Playground
- Reference branch: main
- Audited commit: b9be205ac64488c23504ca42e5ec790337adeec3
- Role: MuJoCo simulation and policy training reference.
- License status: no root LICENSE file was present in the inspected main tree. Some source files contain Apache-2.0 headers, but verify each file and asset before copying. Do not assume the entire repository or its binary assets share one license.

## Community armor-cover reference

- Source: Open Duck Mini V2, `print/mods/v2_Jaimes_Mods`
- Author: Jaime Machuca (jmachuca77)
- Purpose: alternative body and leg covers, cable guides and emergency-stop panel.
- Attribution: the mod README asks users to retain attribution and notes that the covers alter mass distribution and may reduce stability with the existing RL policy.
- This mod is a reference only. It is not the GPT-Mecha original light-knight armor design.

## Attribution rules

- Do not remove upstream copyright or license notices.
- Do not imply that upstream authors endorse GPT-Mecha 40.
- Keep imported files in a clearly identified third_party directory.
- Record source repository, commit, file path, original license and any modifications.
- Do not place upstream CAD, meshes, binaries, policies or source code under a new project license.
- If a file's license is unclear, link to it instead of copying it until its terms are verified.

This repository's original files will receive explicit per-directory licensing in a later change. A single root license must not be used to relicense third-party materials.
