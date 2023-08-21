from flask import Flask, render_template

template_dir = "./templates"

app = Flask(__name__,template_folder=template_dir)


@app.route("/monitor_data")
def data_quality_report():

    """
    Returns data_quality_dashboard as html
    """

    return render_template("data_and_target_drift_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3600)
