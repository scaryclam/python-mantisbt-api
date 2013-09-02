from suds.client import Client


class MantisClient(object):
    def __init__(self, username, password, server_url):
        self.conn = Client(server_url)
        self.username = username
        self.password = password

    def get_users_projects(self):
        projects = self.conn.service.mc_projects_get_user_accessible(
                self.username, self.password)
        project_list = []
        for project in projects:
            project_list.append(Project(project))
        return project_list

    def project_get_issues(self, project, page=1, window_size=100):
        issues = project.get_issues(
                self.conn, self.username, self.password,
                page=page, window_size=window_size)
        return issues


class MantisObj(object):
    def __init__(self, obj):
        self.id = obj.id
        self.name = obj.name


class MantisUser(object):
    def __init__(self, user):
        self.user_id = user.id
        self.username = user.name
        self.real_name = user.real_name
        self.email = user.email


class MantisNote(object):
    def __init__(self, note):
        self.note_id = note.id
        self.reporter = MantisUser(note.reporter)
        self.text = note.text
        self.view_state = MantisObj(note.view_state)
        self.date_submitted = note.date_submitted
        self.last_modified = note.last_modified
        self.time_tracking = note.time_tracking
        self.note_type = note.note_type
        self.note_attr = note.note_attr


class Project(object):
    def __init__(self, data):
        self.project_id = data.id
        self.name = data.name
        self.status = MantisObj(data.status)
        self.enabled = data.enabled
        self.view_state = MantisObj(data.view_state)
        self.access_min = MantisObj(data.access_min)
        self.file_path = data.file_path
        self.description = data.description
        self.subprojects = data.subprojects

    def get_issues(self, conn, username, password, page=1, window_size=100):
        issues = conn.service.mc_project_get_issues(username, password,
                                                    self.project_id,
                                                    page, window_size)
        import ipdb
        ipdb.set_trace()
        issue_list = []
        for issue in issues:
            issue_list.append(Issue(issue))
        return issue_list



class Issue(object):
    def __init__(self, data):
        self.issue_id = data.id
        self.view_state = MantisObj(data.view_state)
        self.last_updated = data.last_updated
        self.project = MantisObj(data.project)
        self.category = data.category
        self.priority = MantisObj(data.priority)
        self.severity = MantisObj(data.severity)
        self.status = MantisObj(data.status)
        self.reporter = MantisUser(data.reporter)
        self.summary = data.summary
        self.version = getattr(data, 'version', '0')
        self.reproducibility = data.reproducibility
        self.date_submitted = data.date_submitted
        self.sponsorship_total = data.sponsorship_total
        self.handler = MantisUser(data.handler)
        self.projection = MantisObj(data.projection)
        self.eta = MantisObj(data.eta)
        self.resolution = MantisObj(data.resolution)
        self.target_version = getattr(data, 'target_version', '0')
        self.description = data.description
        self.attachments = data.attachments
        self.notes = [MantisNote(note_data) for note_data in getattr(data, 'notes', [])]

