def init_app(app):
    from web_flask.0_hello_route import hello_route
    from web_flask.1_hbnb_route import hbnb_route
    from web_flask.2_c_route import c_route
    from web_flask.3_python_route import python_route
    from web_flask.4_number_route import number_route
    from web_flask.5_number_template import number_template
    from web_flask.6_number_odd_or_even import number_odd_or_even
    from web_flask.7_states_list import states_list
    from web_flask.8_cities_by_states import cities_by_states
    from web_flask.9_states import states
    from web_flask.10_hbnb_filters import hbnb_filters

    app.register_blueprint(hello_route)
    app.register_blueprint(hbnb_route)
    app.register_blueprint(c_route)
    app.register_blueprint(python_route)
    app.register_blueprint(number_route)
    app.register_blueprint(number_template)
    app.register_blueprint(number_odd_or_even)
    app.register_blueprint(states_list)
    app.register_blueprint(cities_by_states)
    app.register_blueprint(states)
    app.register_blueprint(hbnb_filters)
