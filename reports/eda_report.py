from flask import Flask, render_template

template_dir = "./templates"

app = Flask(__name__,template_folder=template_dir)


@app.route("/eda")
def data_quality_report():

    """
    Returns data_quality_dashboard as html
    """

    return render_template("eda_report.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3500)
