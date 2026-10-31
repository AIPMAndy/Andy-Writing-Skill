# GitHub release and maintenance

Repository: https://github.com/AIPMAndy/Andy-Writing-Skill

This repository is published as a standalone open-source project. To update code after editing locally, create a feature branch and open a pull request, or push changes with appropriate access:

```bash
git clone https://github.com/AIPMAndy/Andy-Writing-Skill.git
cd Andy-Writing-Skill
python3 -m unittest discover -s tests -v
```

Before a release:

- Verify tests, documentation, and compatibility with supported Agent clients.
- Check LICENSE and permissions for any upstream adaptations.
- Never commit credentials or real customer data.
- Review generated writing examples for accuracy and permissions.
- Do not present linked upstream Skills as bundled or already executed.
