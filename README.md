# Software-Engr-Project [Click here for project](https://andrew03f.github.io/Software-Engr-Project/)
## Update
This project uses `flask`, a popular python library for web development. To install it and get an idea of
how it works, see this [link](https://code.visualstudio.com/docs/python/tutorial-flask).

## Workflow
### 1.) Branch from `main` with:
<pre>
git checkout main
git pull
git checkout -b name-of-feature
</pre>

### 2.) Edit the code and make some commits

### 3.) Test it locally (manually)
make sure you working directory is the same as the directory the `quizapp` directory, then run:
<pre>
  flask --app quizapp run --debug
</pre>

### 4.) Push to remote repository
make sure that the branch you on is your feature branch. The this will report the branch your on
<pre>
git status
</pre>
Push it(once you make commits):
<pre>
git push origin name-of-your-feature
</pre>

