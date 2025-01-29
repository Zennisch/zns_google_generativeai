from typing import Iterable

from google.generativeai import configure, GenerativeModel, ChatSession
from google.generativeai.types import safety_types, generation_types, content_types
from zns_logging.LogUtility import log_and_raise


class GenaiSessionManager:
    def __init__(
        self,
        api_key: str,
        *,
        model_name: str = "gemini-1.5-flash",
        safety_settings: safety_types.SafetySettingOptions | None = None,
        generation_config: generation_types.GenerationConfigType | None = None,
        tools: content_types.FunctionLibraryType | None = None,
        tool_config: content_types.ToolConfigType | None = None,
        system_instruction: content_types.ContentType | None = None,
    ):
        self.__api_key = api_key
        configure(api_key=self.__api_key)

        self.__model_name = model_name
        self.__safety_settings = safety_settings
        self.__generation_config = generation_config
        self.__tools = tools
        self.__tool_config = tool_config
        self.__system_instruction = system_instruction

        self.__model: GenerativeModel | None = None
        self.__reload_model()

    def set_api_key(self, value: str):
        if not isinstance(value, str):
            log_and_raise(__name__, "The value must be a string.", ValueError)
        self.__api_key = value
        configure(api_key=self.__api_key)

    def set_model_name(self, value: str):
        if not isinstance(value, str):
            log_and_raise(__name__, "The value must be a string.", ValueError)
        self.__model_name = value
        self.__reload_model()

    def set_safety_settings(self, value: safety_types.SafetySettingOptions):
        self.__safety_settings = value
        self.__reload_model()

    def set_generation_config(self, value: generation_types.GenerationConfigType):
        self.__generation_config = value
        self.__reload_model()

    def set_tools(self, value: content_types.FunctionLibraryType):
        self.__tools = value
        self.__reload_model()

    def set_tool_config(self, value: content_types.ToolConfigType):
        self.__tool_config = value
        self.__reload_model()

    def set_system_instruction(self, value: content_types.ContentType):
        self.__system_instruction = value
        self.__reload_model()

    def __reload_model(self):
        self.__model = GenerativeModel(
            model_name=self.__model_name,
            safety_settings=self.__safety_settings,
            generation_config=self.__generation_config,
            tools=self.__tools,
            tool_config=self.__tool_config,
            system_instruction=self.__system_instruction,
        )

    def create_chat_session(self) -> ChatSession:
        if self.__model is None:
            log_and_raise(__name__, "The model is not initialized.", ValueError)
        return ChatSession(model=self.__model)

    def create_chat_session_with_history(
        self,
        history: Iterable[content_types.StrictContentType] | None = None,
    ) -> ChatSession:
        if self.__model is None:
            log_and_raise(__name__, "The model is not initialized.", ValueError)
        return ChatSession(model=self.__model, history=history)

__all__ = ["GenaiSessionManager"]
