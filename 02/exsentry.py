import sentry_sdk
sentry_sdk.init(
    dsn="https://d1e8de69b5d04039b8453350c623a9dc@o393307.ingest.sentry.io/5677662",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
