pytest -v -s --browser chrome -m sanity
rem pytest --browser chrome -m regression
rem pytest --browser chrome -m "sanity and regression"

rem pytest -n 3 --browser chrome