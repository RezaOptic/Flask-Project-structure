from flask import Flask, render_template
from project.config import DefaultConfig
from project.helpers.exceptions import NotFoundError, ForbiddenError, NetworkError

default_app_name = "APP NAME"


def create_app(config=None, app_name=default_app_name):
    app = Flask(app_name)
    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    return app


def configure_app(app, config):
    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object(DefaultConfig)


def configure_blueprints(app):
    # api_versions = app.config["API_VERSIONS"]
    # for api_version in api_versions:
    #     blueprints = __import__("project.controllers.{}".format(api_version), fromlist=[api_version])
    #     app.register_blueprint(blueprints.api_bp)
    # app.register_blueprint(bp)
    pass


def configure_extensions(app):
    pass


def configure_custom_errors(app):
    pass

    # @app.errorhandler(NotFoundError)
    # def validation_error():
    #     _error = dict(error_code=599, error_message='اطلاعات ارسالی معتبر نمی‌باشد')
    #     return render_template("error.html", _error)
    #
    # @app.errorhandler(ForbiddenError)
    # def validation_error():
    #     _error = dict(error_code=599, error_message='اطلاعات ارسالی معتبر نمی‌باشد')
    #     return render_template("error.html", _error)
    #
    # @app.errorhandler(NetworkError)
    # def network_error():
    #     _error = dict(error_code=599, error_message='اطلاعات ارسالی معتبر نمی‌باشد')
    #     return render_template("error.html", _error)

    # @app.errorhandler(NotFoundError)
    # def validation_error(error):
    #     _error = dict(message='اطلاعات مورد نظر یافت نشد')
    #     if error.field and error.error:
    #         _error['errors'] = {
    #             error.field: [error.error]
    #         }
    #     elif error.error:
    #         _error['message'] = error.error
    #     return jsonify(_error), 404
    #
    # @app.errorhandler(ForbiddenError)
    # def validation_error(error):
    #     _error = dict(message='شما به این قسمت دسترسی ندارید')
    #     if error.field and error.error:
    #         _error['errors'] = {
    #             error.field: [error.error]
    #         }
    #     elif error.error:
    #         _error['message'] = error.error
    #     return jsonify(_error), 403
