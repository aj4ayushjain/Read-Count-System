from flask_table import Table, Col, LinkCol, create_table

class Results(Table):

    id = Col('Id',show=False)
    title = Col('Title')
    content = Col('A',show=False)
    open = LinkCol('Open--Click here', 'main.open', url_kwargs=dict(id='id'))