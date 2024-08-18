
Traffic:
- Crawl
- Live Ingestion

Crawl Scenarios:
- Primary -> Stamp: initial crawl, including upscaling
- DRI command
- Repair system, e.g. range crawl
- Ruminator: source reprocess

Owned by [[Data plane]] team

crawl filter

https://portal.microsoftgeneva.com/s/3BB21841?overrides=[{"query":"//*[id='DeployRing']","key":"value","replacement":"sdfv2"},{"query":"//*[id='Feeder']","key":"value","replacement":"Crawler"},{"query":"//*[id='Forest']","key":"value","replacement":""},{"query":"//*[id='AvailabilityGroup']","key":"value","replacement":""}]%20

# Slow throughput

TBA(WLM) -> Crawler -> TenantSearch (FlowControl) -> Hub -> Bus/Grain(WLM) (FlowControl) -> Rest (WLM) -> Store

NRT path
DLQ

Work with DP
[Proposals and followups](https://microsoft.sharepoint.com/:fl:/s/2192b384-901d-49c7-81fa-ae4cf97dc8e8/ESax0xp5_SVJnr_A0JQmAoYBN_LF7cjmkF1GrSbGeAbzQg?e=b74ELs&nav=cz0lMkZzaXRlcyUyRjIxOTJiMzg0LTkwMWQtNDljNy04MWZhLWFlNGNmOTdkYzhlOCZkPWIhR2hGc0NXWkVNMGVqN0hQYzRsLWJRbGNzYWtpbDgwbE9nZEk3Q2xpNzNRRzJSZ2Z6bVZXRFM1U2RDYjVKVF9QSiZmPTAxN0NSM1Q0WkdXSEpSVTZQNUVWRVo1UDZBMkNLQ01BVUcmYz0lMkYmZmx1aWQ9MSZhPUxvb3BBcHAmcD0lNDBmbHVpZHglMkZsb29wLXBhZ2UtY29udGFpbmVyJng9JTdCJTIydyUyMiUzQSUyMlQwUlRVSHh0YVdOeWIzTnZablF1YzJoaGNtVndiMmx1ZEM1amIyMThZaUZIYUVaelExZGFSVTB3WldvM1NGQmpOR3d0WWxGc1kzTmhhMmxzT0RCc1QyZGtTVGREYkdrM00xRkhNbEpuWm5wdFZsZEVVelZUWkVOaU5VcFVYMUJLZkRBeE4wTlNNMVEwV2xwWlRFTmFURkpIUXpWU1IxcFJOa1pFVWtZMlFscFdXalUlM0QlMjIlMkMlMjJpJTIyJTNBJTIyZGJjNmJmOWYtOGVlYS00ODc0LTk0Y2QtYTEyZDNlZTdiZmEzJTIyJTdE)

Item processor availability - report in MSR
[Item Processors | Jarvis (microsoftgeneva.com)](https://portal.microsoftgeneva.com/dashboard/GriffinKernel/Partner%2520Dashboards/All%2520Partners/Item%2520Processors?overrides=[%7B%22query%22:%22//*[id%3D%27Environment%27]%22,%22key%22:%22value%22,%22replacement%22:%22WW%22%7D,%7B%22query%22:%22//*[id%3D%27ProcessorName%27]%22,%22key%22:%22value%22,%22replacement%22:%22TenantSearchFolderMoveItemCrawlProcessor,TenantSearchItemCrawlProcessor,RuminatorDynamicCrawler%22%7D]%20)