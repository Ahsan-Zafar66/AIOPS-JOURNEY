from flask import Flask,render_template,request
from jira import JIRA


app = Flask(__name__)

@app.route("/")
def webpage():
    return render_template("page.html")

@app.route("/information",methods=["POST","GET"])
def information():
    if request.method == "POST":
        # when user will fill the form, each section will get value from user, now I am extracting that value from form
        project_data = request.form["project"]
        issue_data = request.form["issue"]
        reporter_data = request.form["reporter"]
        priority_data = request.form["priority"]
        summary_data = request.form["summary"]
        description_data = request.form["description"]

        print("Values enter by uder for fields are")
        print(f"Project: {project_data}, issue: {issue_data},reporter: {reporter_data},priority:{priority_data},summary: {summary_data},description: {description_data}")



        user = "use your email"
        api = "use your api token"
        myserver = "use atlassian project url"

        # establishing the connection with jira using username and api token
        jira = JIRA(server=myserver,basic_auth=(user,api))


        issue_details = {
    'project':{'key':project_data},
    'issuetype':{'name':issue_data},
    # make sure if reporter is available on the screen where you are creating issue
    #'reporter': {"accountId":reporter_data},
    "priority": {"name":priority_data},
    'description': description_data,
    'summary': summary_data,}
    
    # some projects does not have timetracking field by default, go to screen and add timetracking field for that screen
    # method # 1
        # issue = jira.create_issue(project=project_data,issuetype=issue_data,description=description_data,summary=summary_data,reporter={"id":reporter_data},priority={"name":priority_data})
        
        
        issue = jira.create_issue(issue_details)
        print(issue)



    else:
        print("Not found")
    
    return "Issue has been created succesfully"



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")