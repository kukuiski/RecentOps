from functools import wraps
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def log(filename: str = '') -> Callable[[F], F]:
    def log_decorator(function: F) -> F:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                # Логируем успешное выполнение
                log_message = f"{function.__name__} ok\n"
                write_log(log_message, filename)
                return result
            except Exception as e:
                # Логируем ошибку
                log_message = f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n"
                write_log(log_message, filename)
                raise e

        return wrapper  # type: ignore

    return log_decorator


def write_log(message: str, filename: str) -> None:
    """Функция для записи лога в файл или в консоль."""
    if filename:
        with open(filename, 'a') as f:
            f.write(message)
    else:
        print(message, end="")
