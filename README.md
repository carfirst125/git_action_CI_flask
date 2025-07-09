# git_action_CI_flask

## CI

CI using Github Action, using Python workflow of github actions.

CI trigger when push and pull request to main branch

CI run pytest to unit test.

[STATUS][PASS]

## CD

your-project/
├── app.py                # Flask app
├── Dockerfile            # build image từ app
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions CD workflow
├── requirements.txt      # chứa Flask
