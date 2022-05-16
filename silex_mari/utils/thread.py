from site import execusercustomize
from typing import Callable

import mari
from silex_client.utils.thread import ExecutionInThread

class MariExecutionInMainThread(ExecutionInThread):
    def execute_wrapped_function(self, wrapped_function: Callable):
        nuke.executeInMainThread(wrapped_function)
        
execute_in_main_thread = NukeExecutionInMainThread()