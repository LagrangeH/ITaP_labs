def statistic(*functions, to_file: bool = True, calls: int = 1, timeunit: float = .01):
    """
    # Description
    This is a decorator that displays execution statistics for a function or
    functions that take the same positional arguments.
    Use `snakeviz filename.prof` to view.

    # Usage

    :param timeunit: Multiplier for nanoseconds.
    :param calls: How many calls will be performed.
    :param functions: Function or functions that take the same arguments.
    :param to_file: If to_file is True, save statistics to .prof file (e.g. scriptName_funcName.prof)
    and show it in browser, else print.
    :return: Decorated function
    """

    def wrapper(**kwargs):
        """
        :param kwargs: Positional arguments for decorated functions.
        :return:
        """
        import cProfile
        import pstats
        import subprocess
        import time

        from datetime import datetime as dt
        from pathlib import Path

        def _all_functions(*funcs):
            """
            This function combines functions to visualize them in profiling.

            :param funcs: Function or functions that take the same positional arguments.
            :return: None
            """
            for func in funcs:
                func(**kwargs)

        stats = pstats.Stats()

        for _ in range(calls):

            # Call and profile decorating functions
            with cProfile.Profile(timer=time.monotonic_ns, timeunit=timeunit) as pr:
                _all_functions(*functions)

            stats.add(pr)

        # Sort statistics by time
        stats.sort_stats(pstats.SortKey.TIME)

        if not to_file:
            stats.print_stats()
        else:
            import os
            from __main__ import __file__

            # Create directory for profiling if it doesn't exist
            profile_dir = Path('./profiling')
            if not profile_dir.exists():
                os.mkdir(profile_dir)

            # Save profiling to a file
            filename = f'./profiling/{Path(__file__).stem}_{dt.now().isoformat()}.prof'
            stats.dump_stats(filename=filename)

            # Run shankeviz web server and shut it down after 3 seconds
            try:
                subprocess.run(f"snakeviz {filename}", shell=True, timeout=3.0)
            except subprocess.TimeoutExpired:
                subprocess.run('exit', shell=True)
                print("snakeviz web server has been shut down")
            except (KeyboardInterrupt, SystemExit):
                subprocess.run('exit', shell=True)
                exit(0)

    return wrapper
