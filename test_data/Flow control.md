
# Overview
![[Pasted image 20230918182123.png]]
P1/P2 traffic is not flow controlled

Request -> Issue -> Report

# Documents

[FlowControl enhancement opportunities.docx](https://microsoftapc-my.sharepoint.com/:w:/g/personal/chji_microsoft_com/EaYznuN_4LNKgCCr-DysTw4Beed7Ix0wfJ8YH4P412aNng?e=0nSObu)

## Prediction accuracy

Mail: RE: Improving prediction accuracy with BUS metrics (WAS: Re: [PROD] Sev 3: ID 384085851: Forest-wide memory over threshold for: 
Mail: Consistent Routing for FlowControl

[Flow Control Prediction Accuracy V2.docx](https://microsoft-my.sharepoint-df.com/:w:/p/arianetsai/EfUZwnSvs0hKnjhH34mjz_0BLI9QA7ZRwwJmpwV1PzE8xw?e=ywb7ce)
[FC first-line metrics.docx](https://microsoftapc-my.sharepoint.com/:w:/g/personal/zhangning_microsoft_com/EXeHq53w3kdPuiydx118JvsB-TZ_TYYpArbER9PM2Os3xQ?e=DJK7qc)
[Metrics for FlowControl Service health.docx](https://microsoft.sharepoint-df.com/:w:/s/M365CoreSearchExtensibilityTeam/EYtnI2ZuWbpHuCINdf6acBAB31HQZtSb2udMTPoFVTPLgQ?e=pQ1MjH)
[SLA of FlowControl Service.docx](https://microsoftapc-my.sharepoint.com/:w:/g/personal/guangmiaoguo_microsoft_com/Ed0OV9wAGzBEoYzXkKMp1xMB9ZqHo74Lqoz3075qrigEGA?e=XdhQbc)
[Prediction Accuracy Results](onenote:https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/SiteAssets/M365%20Core%20Search%20Extensibility%20Team%20Notebook/FlowControl/Optics.one#Prediction%20Accuracy%20Results&section-id={48328D71-B362-48AE-802D-8566D5DB363E}&page-id={0F99F02E-5935-4CD3-B5CA-98371F69109C}&end)  ([Web view](https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/_layouts/OneNote.aspx?id=%2Fsites%2FM365CoreSearchExtensibilityTeam%2FSiteAssets%2FM365%20Core%20Search%20Extensibility%20Team%20Notebook&wd=target%28FlowControl%2FOptics.one%7C48328D71-B362-48AE-802D-8566D5DB363E%2FPrediction%20Accuracy%20Results%7C0F99F02E-5935-4CD3-B5CA-98371F69109C%2F%29))
[BusSignalIntegration.docx](https://microsoftapc-my.sharepoint.com/:w:/g/personal/chji_microsoft_com/EUfoJkyga8FPr45SrRLws7oBGIbIVdpHZWUItd_WWXqr7w?e=yP1H0d)

Improvement points:
Wrong decision on throttling, the algorithm is vulnerable and not transparent on decision making
Too many sev 3 alerts, no right paging alert to indicate 
Use token generated from token from token algorithm to verify the algorithm itself. Better to use external signals to verify the algorithm effectiveness
Disaster recovery plan
Static strategy
flowcontrol, need way to suppress and also corelate

## Tech

[FC Tech Findings](onenote:https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/SiteAssets/M365%20Core%20Search%20Extensibility%20Team%20Notebook/FlowControl/Development.one#FC%20Tech%20Findings&section-id={A8E8690C-7A3D-45CF-8541-CCFF1D84AB45}&page-id={DDCA4707-F2E6-D543-8AFB-62A289EC0EDC}&end)  ([Web view](https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/_layouts/OneNote.aspx?id=%2Fsites%2FM365CoreSearchExtensibilityTeam%2FSiteAssets%2FM365%20Core%20Search%20Extensibility%20Team%20Notebook&wd=target%28FlowControl%2FDevelopment.one%7CA8E8690C-7A3D-45CF-8541-CCFF1D84AB45%2FFC%20Tech%20Findings%7CDDCA4707-F2E6-D543-8AFB-62A289EC0EDC%2F%29))

**Kalman filter algorithm**
uses a series of measurements observed over time, including [statistical noise](https://en.wikipedia.org/wiki/Statistical_noise "Statistical noise") and other inaccuracies, and produces estimates of unknown variables that tend to be more accurate than those based on a single measurement alone, by estimating a [joint probability distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution "Joint probability distribution") over the variables for each timeframe.
https://thekalmanfilter.com/kalman-filter-explained-simply/
The real power of the Kalman Filter is not smoothing measurements. It is the ability to estimate system parameters that can not be measured or observed with accuracy. Optimal estimation algorithm, you cannot always directly measure something, then rely on indirect measurement, or noisy measurement
state observers

Kalman gain = Eest / (Eest + Emea)
Estimate is stable, measurement are inaccurate K = 0
Measurement is accurate, estimate unstable K = 1

**PUMA**
PUMA stands for Process Utilization Manager and Accounting  [PUMA](https://o365exchange.visualstudio.com/O365%20Core/_wiki/wikis/O365%20Core.wiki/40828/PUMA)
PUMA cansoft cap service memory/ CPU time usages. 

FlowControl Onboarding Doc: [Onboarding](onenote:https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/SiteAssets/M365%20Core%20Search%20Extensibility%20Team%20Notebook/FlowControl/Onboarding.one#section-id=%7BF6ECB8A1-BE8B-4371-A17B-AE7EB7B1A849%7D&end "onenote:https://microsoft.sharepoint-df.com/sites/m365coresearchextensibilityteam/siteassets/m365%20core%20search%20extensibility%20team%20notebook/flowcontrol/onboarding.one#section-id=%7bf6ecb8a1-be8b-4371-a17b-ae7eb7b1a849%7d&end")  ([Web view](https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/_layouts/OneNote.aspx?id=%2Fsites%2FM365CoreSearchExtensibilityTeam%2FSiteAssets%2FM365%20Core%20Search%20Extensibility%20Team%20Notebook&wd=target%28FlowControl%2FOnboarding.one%7CF6ECB8A1-BE8B-4371-A17B-AE7EB7B1A849%2F%29&xsdata=MDV8MDF8fDQyODg4N2E3NmQxNTQ0NTg5ODFmMDhkYjUwNDFiMGM3fDcyZjk4OGJmODZmMTQxYWY5MWFiMmQ3Y2QwMTFkYjQ3fDB8MHw2MzgxOTIwMTUyNzIwMjQwOTV8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxNVFk0TXpZd05EY3lOVGN6T1RzeE5qZ3pOakEwTnpJMU56TTVPekU1T2pJeE1EVXpPRGt5TFdFNVpUWXROREZqWVMwNE5tWTBMVE13TmpVM1pUVXlaalE1T1Y5a1lUWXpORGRtTmkwNFpUTmxMVFEzWldNdE9HUTNNQzB4WkRBek1qYzBZekpoWmpKQWRXNXhMbWRpYkM1emNHRmpaWE09fGI0OGI5OGM5OGM3NDQ2Mzk5ODFmMDhkYjUwNDFiMGM3fGVhZmMzNWI0YWM5MTQ0MDZiM2QxNjRkYjNjNjI2ODE3&sdata=UFU4akVBTWlRS2NhMEZZSTZsS0xYcnpLZGxGSVRvanNYZDlxZ2RFbGRpST0%3D&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2Cbinweiwu%40microsoft.com "https://microsoft.sharepoint-df.com/sites/m365coresearchextensibilityteam/_layouts/onenote.aspx?id=%2fsites%2fm365coresearchextensibilityteam%2fsiteassets%2fm365%20core%20search%20extensibility%20team%20notebook&wd=target%28flowcontrol%2fonboarding.one%7cf6ecb8a1-be8b-4371-a17b-ae7eb7b1a849%2f%29&xsdata=mdv8mdf8fdqyodg4n2e3nmqxntq0ntg5odfmmdhkyjuwndfimgm3fdcyzjk4ogjmodzmmtqxywy5mwfimmq3y2qwmtfkyjq3fdb8mhw2mzgxotiwmtuynziwmjqwotv8vw5rbm93bnxwr1zoylhovfpxtjfjbwwwzvzobgnuwnbzmly4zxlkv0lqb2lnqzr3tgpbd01eqwlmq0prswpvavyybhvneklptenkqlrpstzjazkwyudweulpd2lwmvfpt2pfegzrpt18mxxnvfk0txpzd05ey3lovgn6t1rzee5qz3poakewtnpjmu56ttvpeku1t2pjee1evxpprgt5tfdfnvpuwxrorezqwvmwne5twtbmve13tmpvm1puvxlaale1t1y5a1luwxporgrttmkwnfputmxmvfezwldnde9hutnnqzb4wkrbek1qyzbzekpowmpkqwrxnxhmbwrpykm1emnhrmpawe09fgi0ogi5ogm5ogm3ndq2mzk5odfmmdhkyjuwndfimgm3fgvhzmmznwi0ywm5mtq0mdzim2qxnjrkyjnjnji2ode3&sdata=ufu4akvbtwlrs2nhmezzstzss0xycnplzgxgsvrvannyzdlxz2rfbgrpst0%3d&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2cbinweiwu%40microsoft.com"))
FlowControl 101: [Flow Control 101](onenote:https://microsoftapc.sharepoint.com/teams/M365CoreSearchContentUnderstandingTeamSuzhou/SiteAssets/M365%20Core%20Search%20Content%20Understanding%20Team,%20Suzhou%20Notebook/Knowledge%20Sharing.one#Flow%20Control%20101&section-id=%7BA5AF587A-5EDE-4DC7-AC6C-88765ABF1F0A%7D&page-id=%7BE31C4C29-8727-4A88-8301-A2650F2E7427%7D&end "onenote:https://microsoftapc.sharepoint.com/teams/m365coresearchcontentunderstandingteamsuzhou/siteassets/m365%20core%20search%20content%20understanding%20team,%20suzhou%20notebook/knowledge%20sharing.one#flow%20control%20101&section-id=%7ba5af587a-5ede-4dc7-ac6c-88765abf1f0a%7d&page-id=%7be31c4c29-8727-4a88-8301-a2650f2e7427%7d&end")  ([Web view](https://microsoftapc.sharepoint.com/teams/M365CoreSearchContentUnderstandingTeamSuzhou/_layouts/OneNote.aspx?id=%2Fteams%2FM365CoreSearchContentUnderstandingTeamSuzhou%2FSiteAssets%2FM365%20Core%20Search%20Content%20Understanding%20Team%2C%20Suzhou%20Notebook&wd=target%28Knowledge%20Sharing.one%7CA5AF587A-5EDE-4DC7-AC6C-88765ABF1F0A%2FFlow%20Control%20101%7CE31C4C29-8727-4A88-8301-A2650F2E7427%2F%29&xsdata=MDV8MDF8fDQyODg4N2E3NmQxNTQ0NTg5ODFmMDhkYjUwNDFiMGM3fDcyZjk4OGJmODZmMTQxYWY5MWFiMmQ3Y2QwMTFkYjQ3fDB8MHw2MzgxOTIwMTUyNzIwMjQwOTV8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxNVFk0TXpZd05EY3lOVGN6T1RzeE5qZ3pOakEwTnpJMU56TTVPekU1T2pJeE1EVXpPRGt5TFdFNVpUWXROREZqWVMwNE5tWTBMVE13TmpVM1pUVXlaalE1T1Y5a1lUWXpORGRtTmkwNFpUTmxMVFEzWldNdE9HUTNNQzB4WkRBek1qYzBZekpoWmpKQWRXNXhMbWRpYkM1emNHRmpaWE09fGI0OGI5OGM5OGM3NDQ2Mzk5ODFmMDhkYjUwNDFiMGM3fGVhZmMzNWI0YWM5MTQ0MDZiM2QxNjRkYjNjNjI2ODE3&sdata=aFFqWFhMYS9OQmM2UVdpbWZaOWFSSUpqcWF2bXQzRk1WZ3pqcmdEZTNVMD0%3D&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2Cbinweiwu%40microsoft.com "https://microsoftapc.sharepoint.com/teams/m365coresearchcontentunderstandingteamsuzhou/_layouts/onenote.aspx?id=%2fteams%2fm365coresearchcontentunderstandingteamsuzhou%2fsiteassets%2fm365%20core%20search%20content%20understanding%20team%2c%20suzhou%20notebook&wd=target%28knowledge%20sharing.one%7ca5af587a-5ede-4dc7-ac6c-88765abf1f0a%2fflow%20control%20101%7ce31c4c29-8727-4a88-8301-a2650f2e7427%2f%29&xsdata=mdv8mdf8fdqyodg4n2e3nmqxntq0ntg5odfmmdhkyjuwndfimgm3fdcyzjk4ogjmodzmmtqxywy5mwfimmq3y2qwmtfkyjq3fdb8mhw2mzgxotiwmtuynziwmjqwotv8vw5rbm93bnxwr1zoylhovfpxtjfjbwwwzvzobgnuwnbzmly4zxlkv0lqb2lnqzr3tgpbd01eqwlmq0prswpvavyybhvneklptenkqlrpstzjazkwyudweulpd2lwmvfpt2pfegzrpt18mxxnvfk0txpzd05ey3lovgn6t1rzee5qz3poakewtnpjmu56ttvpeku1t2pjee1evxpprgt5tfdfnvpuwxrorezqwvmwne5twtbmve13tmpvm1puvxlaale1t1y5a1luwxporgrttmkwnfputmxmvfezwldnde9hutnnqzb4wkrbek1qyzbzekpowmpkqwrxnxhmbwrpykm1emnhrmpawe09fgi0ogi5ogm5ogm3ndq2mzk5odfmmdhkyjuwndfimgm3fgvhzmmznwi0ywm5mtq0mdzim2qxnjrkyjnjnji2ode3&sdata=affqwfhmys9oqmm2uvdpbwzaowfssupqcwf2bxqzrk1wz3pqcmdeztnvmd0%3d&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2cbinweiwu%40microsoft.com"))
[Flow Control Service for ASC - Design Spec.docx](https://microsoft.sharepoint-df.com/:w:/s/M365CoreSearchExtensibilityTeam/EW8p4TbOcqpOgXu0___hPuoB3EFkam-BoGOeQNTQ_X79cQ?e=xweWOE)

LEB: static token refill
LEB + dynamic token strategy

Further OOM issue handling: Shall push back of requests

## [[SCI]]

[Flow control SCI doc](https://microsoft-my.sharepoint-df.com/:w:/p/radhikajoshi/EcDXEbK7c1FAvPyqw1Yz8p4B0qVwslHIzLC21wEDD0HytQ?e=mbTcAS)

## Consistent Routing

Crash count
[https://portal.microsoftgeneva.com/s/B9D3E29A](https://portal.microsoftgeneva.com/s/B9D3E29A "https://portal.microsoftgeneva.com/s/b9d3e29a")

Flowcontrol consistency heatmap
[https://msit.powerbi.com/groups/me/reports/855720ac-20b0-455b-aa2d-ddb3b35748d6/ReportSection39733fcbc9eae44a3030?experience=power-bi](https://msit.powerbi.com/groups/me/reports/855720ac-20b0-455b-aa2d-ddb3b35748d6/ReportSection39733fcbc9eae44a3030?experience=power-bi "https://msit.powerbi.com/groups/me/reports/855720ac-20b0-455b-aa2d-ddb3b35748d6/reportsection39733fcbc9eae44a3030?experience=power-bi")

# Enhancements
## Use FC in [[Ruminator]]

## Lack of load testing environment
Especially important for accuracy prediction improvement

# Repo

https://o365exchange.visualstudio.com/O365%20Core/_git/FlowControl

# People

- [[Ning Zhang]]
- [[Guangmiao Guo]]
- [[Jing Chen]]
- [[Longwei Liu]]

People from US side:
- [[Priya Manoharan]]
- Ariana Tsai 
- Radhika Joshi 
- Suyang Jiang
