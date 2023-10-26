# Software-Engr-Project [Click here for project](https://andrew03f.github.io/Software-Engr-Project/)
## Workflow
### 1.) Branch from `main` with:
<pre>
git chekcout main
git pull
git checkout -b name-of-feature
</pre>

### 2.) Edit the code and make some commits


### 3.) Test it locally (manually)
make sure you working directory is the same as the directory containing the file `index.html`, then run:
<pre>
  python3 -m http.server 
</pre>
this is one way to locally serve a website

### 4.) Push to remote repository
make sure that the branch you on is your feature branch. The this will report the branch your on
<pre>
git status
</pre>
Push it(once you make commits):
<pre>
git push origin name-of-your-feature
</pre>

