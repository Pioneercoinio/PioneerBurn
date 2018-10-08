# Pioneercoin burning mechanism

**NOTE** coin burning is not yet active. Do not burn any tokens yet.

The effort to keep the Pioneercoin community centers around transferring
pcoin into PRT, a token on the ethereum network.

This repository contains the information on how to burn your pcoin and ensure
that you receive the correct amount of PRT. This mechanism strives to be 
secure so that only the person owning the original pcoin can nominate the 
ethereum address to receive the PRT.

There are two main transfer methods:
- Using pioneercoin wallet
- Directly from an exchange

Both mechanisms are centered around sending a signed message to the PRT developers.

The message to send must satisfy the json schema [message_schema.json](message_schema.json)