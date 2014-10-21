from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.context_processor
def context_processor():
    def icon(name):
        return '<i class="fa fa-' + name + '"></i>'

    def project_processor(proj, langs, docs=None):
        html = "<h2>" + proj

        for lang in langs:
            html += '<span class="lang">' + lang + '</span>'

        html += '<a class="source" href="https://github.com/erik/' + proj + '">Source</a>'

        if docs:
            html += '<a class="source" href="' + docs + '">Documentation</a>'

        html += '</h2>'
        html += '<hr class="small" />'

        return html

    return dict(project=project_processor, icon=icon)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
