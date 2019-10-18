#!/bin/bash
#
# Compile a French document to PDF and HTML
#
name=HAM20192020

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
  doconce replace "Summary" "Résumé" $1
  doconce replace "Notice" "Note" $1
  doconce replace "Table of contents" "Table des matières" $1
  doconce replace "Contents" "Contenu" $1
  doconce replace "Project" "Projet" $1
  doconce replace "Example" "Exemple" $1
  doconce replace "Warning" "Avertissement" $1
  doconce replace "Hint" "Indication" $1
}
# Note: since Doconce syntax is demonstrated inside !bc/!ec
# blocks we need a few fixes

function editfix {
# Fix selected backslashes inside verbatim envirs that doconce has added
# (only a problem when we want to show full doconce code with
# labels in !bc-!ec envirs as in this presentation).
doconce replace '\label{this:section}' 'label{this:section}' $1
doconce replace '\label{fig1}' 'label{fig1}' $1
doconce replace '\label{demo' 'label{demo' $1
doconce replace '\eqref{eq1}' '(ref{eq1})' $1
doconce replace '\eqref{myeq}' '(ref{myeq})' $1
doconce replace '\eqref{mysec:eq:Dudt}' '(ref{mysec:eq:Dudt})' $1
}


# HTML PLAIN
doconce format html $name $options --html_style=bootswatch_cerulean --pygments_html_style=monokai --html_admon=bootstrap_panel --html_output=index --keep_pygments_html_bg --html_code_style=inherit --html_pre_style=inherit --html_links_in_new_window --debug
common_replacements index.html

cp -r *.html ../

./clean.sh
