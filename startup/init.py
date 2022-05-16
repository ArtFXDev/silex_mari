import mari
from silex_client.action.action_query import ActionQuery
from silex_client.core.context import Context
from silex_client.resolve.config import Config


def create_menus():
    # Get actions names from the config
    actions = [item["name"] for item in Config().actions]

    # Create a menu
    menubar = mari.menus
    shelf = "MainWindow/Silex"
    menubar.addSeparator(shelf)
    m_action = mari.actions

    for action_name in actions:

        current_action = m_action.create(shelf + '/' + action_name, 
                                         f"ActionQuery('{action_name}').execute()")
        # Create an entry in the Silex menu
        menubar.addAction(current_action, shelf)


# Start the WS connection
Context.get().start_services()
create_menus()

# Override Ctrl+S and script save
#save_menu = mari.menu("Mari").findItem("File").findItem("Save Comp")
#save_menu.setScript("ActionQuery('save').execute()")