def task_generate():
    return {
        'actions' : ['doctress css.rst build/css.tex -tbeamer'],
        'targets':['build/css.tex'],
        'file_dep':['css.rst', 'hello.html', 'hello.css'],
    }

def task_pdf():
    return {
            'actions' : ['cp floats.png build/',
                         'cd build && pdflatex -halt-on-error -file-line-error css.tex']
    }
