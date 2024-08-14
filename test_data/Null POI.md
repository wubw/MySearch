
[POI Recrawl Execution.xlsx](https://microsoftapc-my.sharepoint.com/:x:/g/personal/binweiwu_microsoft_com/EUAxXeyndzFJn10ceQRYAPABEIZWdfj9DOxpLDK0zGa5hA?e=a4JBfq)

[Loop paragraph (microsoft.com)](https://loop.microsoft.com/p/eyJ1IjoiaHR0cHM6Ly9taWNyb3NvZnQtbXkuc2hhcmVwb2ludC1kZi5jb20vcGVyc29uYWwveXVtYW5vaGFfbWljcm9zb2Z0X2NvbT9uYXY9Y3owbE1rWndaWEp6YjI1aGJDVXlSbmwxYldGdWIyaGhYMjFwWTNKdmMyOW1kRjlqYjIwbVpEMWlKVEl4ZDIxSmNTMURURlpXVlRaMWRqVmxVR3BhV0ZJNFIwczFaVXcxWW1OdGFFTjJablEzVlRadFYzZHFhbWxuV0dGVWVYZFFURlJhUTBkbVJ6ZHNWVEppTVNabVBUQXhRa0ZPU2tSVlFqWlpTRXBDVVZoSVVVZEdTRXhhVVVsTk4wTTJVell6VERNbVl6MGxNa1ltWVQxTWIyOXdRWEJ3Sm5BOUpUUXdiWE1sTWtadlptWnBZMlV0Wm14MWFXUXRZMjl1ZEdGcGJtVnkifQ%3D%3D?ct=1710466262164&or=Teams-HL)

[Incident 481817078](https://portal.microsofticm.com/imp/v3/incidents/incident/481817078/summary)

[BF Not Indexed Insight - Dashboards - Grafana (azure.com)](https://exstore-evfccyc5f7gxbdd6.eus.grafana.azure.com/d/d9d865fc-2d37-45ec-9004-b26fcaa54ed3/bf-not-indexed-insight?orgId=1&var-Forest=All&var-Tenant=All&var-PHYDB=true&var-BFNotIdxed=10000&var-BFTotal=400000&var-PCTBFNotIdxed=0&from=now-24h&to=now&refresh=1h)

From Jing Fan
[Overall ADO dashboard](https://o365exchange.visualstudio.com/O365%20Core/_dashboards/dashboard/bf38125c-7cdf-4749-9b69-d1e2c4a3a6d5)

# Root cause

FYI Everyone - For awareness: see [[Mengdong Yang]] update on LB - NULLPOI issue: its not just scoped to Phoenix moves

Had a call with Tobias and he corrected some understanding. This is what happened:
1.  in mitigation of an NTK LB add a policy to drop POI to force its regeneration on shard move. that policy is wrongly applied to ASC shard (for ASC we are suppose to always export POI since we don't have the source property that regenerates POI)
2. the "POI drop" policy has been effective since 1/15. any ASC shard move will lose POI. whether it is a MCDB-PHX move or not doesn't matter
3. Bleeding has been stopped. LB team has disabled LB move across the board to stop the bleeding. As stopping LB is not sustainable. LB is making an emergency fix to stop the deliberate POI drop for ASC shard. we will only re-enable LB move after this fix is in. For us, the only thing that matters is bleeding has been stopped
4. LB team enabled at-scale auto move for ASC in a few forests a few days ago that caused POI loss due to point 1. This is the major source of the break due to the scale of ASC move this triggered
5. any manual ASC move after 1/15 will also cause this issue
TLDR: Any manual ASC move after 1/15 will cause POI loss.

[POI Loss Engineering Investments.docx](https://microsoft.sharepoint-df.com/:w:/s/M365CoreSearchExtensibilityTeam/Eahx2QCgSDlKm0xs82JWMtoBWnQac_LvvFhjANcQnNUGAQ?e=AtLxjA)

Mail: Recording for the PIR of the ZAF fiber cut incident

# Track

[Batch tenant repair submission playbook.loop](https://microsoft.sharepoint-df.com/:fl:/g/contentstorage/CSP_14cb9463-73aa-43d9-af6d-5eb970c7e30a/ERSuVS_BqL9HjGKqjdKuXTgB7DTqbeHfKRyVwou9QxB-Bg?e=UjQffz&nav=cz0lMkZjb250ZW50c3RvcmFnZSUyRkNTUF8xNGNiOTQ2My03M2FhLTQzZDktYWY2ZC01ZWI5NzBjN2UzMGEmZD1iJTIxWTVUTEZLcHoyVU92YlY2NWNNZmpDdjVhYi1uVEVtNUFqR0tqTmNJbXp5bS1yUlJIS1dSVFFMbkZQaVczak95cSZmPTAxRDZMVzNaWVVWWktTN1FOSVg1RFlZWVZLUlhKSzRYSlkmYz0lMkYmYT1Mb29wQXBwJnA9JTQwZmx1aWR4JTJGbG9vcC1wYWdlLWNvbnRhaW5lciZ4PSU3QiUyMnclMjIlM0ElMjJUMFJUVUh4dGFXTnliM052Wm5RdWMyaGhjbVZ3YjJsdWRDMWtaaTVqYjIxOFlpRlpOVlJNUmt0d2VqSlZUM1ppVmpZMVkwMW1ha04yTldGaUxXNVVSVzAxUVdwSFMycE9ZMGx0ZW5sdExYSlNVa2hMVjFKVVVVeHVSbEJwVnpOcVQzbHhmREF4UkRaTVZ6TmFOMHRNTkZoUVJqWkJSRTgxUVV3MVVWWkNURVJNU2s0MU16WSUzRCUyMiUyQyUyMmklMjIlM0ElMjI4NzRjMTRjNC0xZDYzLTRhZGUtOWM5OS02ZTA4NDMzN2ViMjElMjIlN0Q%3D)

[2024-03-25 Status update for NULL POI repair.docx (sharepoint-df.com)](https://microsoft-my.sharepoint-df.com/:w:/p/varat/EaGCgsjrls9Fh3RWQjLP11UBhSM5rU57bOuY53Jg44tfwA?e=VX9GXk&isSPOFile=1&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI1MC8yNDAyMjkyNDUxNyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D)

![[Pasted image 20240328144042.png]]

Check remaining NULL POI
https://dataexplorer.azure.com/clusters/substratesearch/databases/SubstrateSearchExceptionEvent?query=H4sIAAAAAAAAA1WNOw4CMQxEe07hEg5BgbbaYleIj6hDYglLcRxiGwnE4dkgUVDO07yZSR6YdhqPFrjqhew2e857oUG82OoN6syh0QvhXOjuOBqywrbz9cg1RMM0SHYu%2Bou98tVnOWDNFMMGrk84EaP2m2VVWsL2ByFo%2FACmlYyMjQAAAA%3D%3D

Check overall crawl completion
https://dataexplorer.azure.com/clusters/o365monweu.westeurope/databases/o365monitoring?query=H4sIAAAAAAAAA42QS2%2FCQAyE7%2F0Vbk5JRduUO4eKPsQBhELuyCSGWNqs0e7yEOLHd5NSaEmCerOsb8aeSUmjdjNCkxVDgzv1viXtxshqIfv5p5IFqrsj7AoyBDbztGGBwQCC9JfyQ1ROZixbGjkqa5%2BpkYysFROc5bOTPMUV3FuHxtkduwKCN8PHeQCo89vMmK1lvfoH2Y%2F7%2FfbDmWiHrC0Ek41SU%2BGE1sjmVamErKs0tHfk%2FSdiSlR8oPwUhfIqnIUB8HIZjmwdcyjlWpGjvAepOFT1suZ6cJnPDtHF%2F6Rk0Qm6qlN4ieOnGB66Lz83byRU%2BjS%2BlJ%2Ffrgh47LTzr9hNWfpiDuRr2WgXRr3vgZv5okZAf8zrw6ut5xp9VVjXF1FLhor%2Fu%2FRUd1837X1pbV9%2BAcIKTyT4AgAA

# Reference

 [PWC incident shifts](onenote:https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/Shared%20Documents/SearchExtensibilityAreasFY19/SearchExtensibilityAreaFY19/ASC.one#PWC%20incident%20shifts&section-id=%7B36EEBA36-B285-4927-A35E-C975363A0CAB%7D&page-id=%7B87672628-7355-4B13-84FA-60C6619CE7D3%7D&end)  ([Web view](https://microsoft.sharepoint-df.com/sites/M365CoreSearchExtensibilityTeam/_layouts/OneNote.aspx?id=%2Fsites%2FM365CoreSearchExtensibilityTeam%2FShared%20Documents%2FSearchExtensibilityAreasFY19%2FSearchExtensibilityAreaFY19&wd=target%28ASC.one%7C36EEBA36-B285-4927-A35E-C975363A0CAB%2FPWC%20incident%20shifts%7C87672628-7355-4B13-84FA-60C6619CE7D3%2F%29&xsdata=MDV8MDJ8fGRmN2QwNTg5MTM5NDQ2NTU5MmZjMDhkYzQ0OTRlMzY4fDcyZjk4OGJmODZmMTQxYWY5MWFiMmQ3Y2QwMTFkYjQ3fDB8MHw2Mzg0NjA2NTM0NDA4OTc3ODh8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPalpqWlRFMVlqTmtaV0kwWVRSa1ltWTVNV00zWlRrek16WXpOell5TVdNeFFIUm9jbVZoWkM1Mk1pOXRaWE56WVdkbGN5OHhOekV3TkRZNE16UXdPVFl3fDI3NGJlZWM2NWQxMzQxNTUzMDdlMDhkYzQ0OTRlMzY2fDNjYTc2NWRjNTg2OTRjZWY5ODFiZmM4ZGQyNmE5ZWZj&sdata=WkdVSTY2Ym9KZ2xYMlFoK2ZFdk5ONzBaNStBcmp3VEVWeDBDSzcwQm5nVT0%3D&ovuser=72f988bf-86f1-41af-91ab-2d7cd011db47%2Cbinweiwu%40microsoft.com))
 [NullPOICountForLongTail.xlsx](https://microsoftapc-my.sharepoint.com/:x:/g/personal/haileywang_microsoft_com/EagMVprdh7NMhzzm9I6bu9cBEx0E_-BWO7cCdF86HbEqJQ?e=0kB3yD)
 