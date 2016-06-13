def task_generate():
    return {
        'actions' : ['doctress css.rst build/css.tex -tbeamer',
                     'cd build/ && pdflatex css.tex']
    }
