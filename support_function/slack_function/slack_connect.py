# # Get application first: https://api.slack.com/apps/A02341UQV2M/oauth?success=1

from slack_sdk import WebClient
client_slack = WebClient(token='xoxb-1216139827667-1906835181267-lntIE0gmV0WAVysAuxd1O9hw') # slack ở MM<3

# # # để DELETE slack post
# # from slack_sdk.errors import SlackApiError
# # import sys

# # try:
# #     # client_slack.chat_postMessage(channel='minchan-testing', text=str(report_crawler_updated)) # slack channel bên M<3
# #     client_slack.chat_postMessage(channel='data-auto-report-error', text=str("testing"))
# # #     # client_slack.chat_postMessage(channel='data-internal', text=str(report_crawler_updated))
# # #     client_slack.chat_delete(channel='C3C7S8KLP',ts='1620275236.101200')
# # #     #client_slack.chat_delete(channel='C3C7S8KLP',ts='1618911613.083000')
# # except SlackApiError as e:
# # ## You will get a SlackApiError if "ok" is False
# #     assert e.response["ok"] is False
# #     assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
# #     print(f"Got an error: {e.response['error']}")
# #     print(f"Got an error: {e.response['ok']}")