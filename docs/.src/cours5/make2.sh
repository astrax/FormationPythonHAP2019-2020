#!/bin/bash
#
# Compile a French document to PDF and HTML
#

name=TD4
# doconce ipynb2doconce $name.ipynb

options="--encoding=utf-8"
opt2="--without_solutions --without_answers"
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

function common_replacements {
  filename=$1
  # Replace English phrases
  # __Summary.__ is needed for identifying the abstract
  doconce replace Summary Résumé $1
  doconce replace Notice "À noter" $1
  doconce replace "Table of contents" "Table des matières" $1
  doconce replace Contents Contenu $1
  doconce replace "Project" "Projet" $1
  doconce replace "Example" "Exemple" $1
  doconce replace "Warning" "Attention" $1
  doconce replace "Hint" "Indication" $1
  doconce replace "Exercise" "Exercice" $1
  doconce replace "Remarks" "Remarques" $1
}

doconce pygmentize $name.do.txt perldoc
# ---------------------
# PDF avec solution
# ----------------------
system doconce format pdflatex $name --latex_code_style=pyg-gray $options --latex_admon=grayicon --latex_admon_title_no_period --latex_style=std --latex_copyright=titlepages
# Tips: http://folk.uio.no/tobiasvl/latex.html
system common_replacements $name.tex

doconce replace '10pt]{' '10pt,french]{' $name.tex
# package [norsk]{label} requires texlive-lang-norwegian package
doconce subst '% insert custom LaTeX commands...' '\usepackage[french]{babel}\n\n% insert custom LaTeX commands...' $name.tex
cp $name.tex ${name}_corr.tex
system pdflatex -shell-escape ${name}_corr
#system bibtex $name
system makeindex ${name}_corr
pdflatex -shell-escape ${name}_corr
pdflatex -shell-escape ${name}_corr
#-------------------
# PDF sans solution
#---------------------
system doconce format pdflatex $name --latex_code_style=pyg-gray $options --latex_admon=grayicon --latex_admon_title_no_period --latex_style=std --latex_copyright=titlepages $opt2
# Tips: http://folk.uio.no/tobiasvl/latex.html
system common_replacements $name.tex

doconce replace '10pt]{' '10pt,french]{' $name.tex
# package [norsk]{label} requires texlive-lang-norwegian package
doconce subst '% insert custom LaTeX commands...' '\usepackage[french]{babel}\n\n% insert custom LaTeX commands...' $name.tex
system pdflatex -shell-escape $name
#system bibtex $name
system makeindex $name
pdflatex -shell-escape $name
pdflatex -shell-escape $name

# HTML
system doconce format html $name --html_style=bootswatch_journal $options
common_replacements $name.html

# Publish
dest=../../pub/$name
if [ ! -d $dest ]; then
mkdir $dest
fi
cp -r *.pdf *.html imgs scripts $dest

./clean.sh
