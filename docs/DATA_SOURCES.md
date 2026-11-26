# Moroccan data sources

This inventory records candidate sources for Phase 1. Phase 0 reviewed public entry points on 2026-11-25 without downloading tender documents. Browser fetch results describe this review session and may differ from a manual visit.

| Candidate | Expected use | Phase 0 access and reuse evidence |
| --- | --- | --- |
| [Moroccan Public Procurement Portal (PMMP)](https://www.marchespublics.gov.ma/pmmp/) | Tender notices, deadlines, attachments and amendments | This route returned HTTP 503. The [official business entry point](https://www.marchespublics.gov.ma/index.php?goto=&page=entreprise.EntrepriseHome) describes notice search and consultation. The [terms page](https://www.marchespublics.gov.ma/?calledFrom=entreprise&page=commun.ConditionsUtilisation) describes portal use and technical requirements. Record-level reuse and permission for automated retrieval remain unverified. |
| [National Commission for Public Procurement (CNCP)](https://www.cncp.gov.ma/) | Institutional guidance and procurement reference material | This entry point timed out. The [government's CNCP page](https://www.sgg.gov.ma/Commissionnationaledelacommandepublique.aspx) provides reference texts, opinions and a documentary collection. Confirm the publisher and terms on the document page. |
| [Moroccan Public Procurement Observatory (OMCP)](https://omcp.tgr.gov.ma/) | Procurement indicators and contextual datasets | Entry point timed out. The [Treasury's OMCP announcement](https://www.tgr.gov.ma/wps/wcm/connect/f0396413-ca65-45c7-8253-0284f452a44b/Communiqu%C3%A9_R%C3%A9union%2BOMCP%2Bfr_27_11_2024%2B%D9%8D%2BVM.pdf?MOD=AJPERES) provides institutional context. Dataset availability and terms remain unverified. |
| [Morocco Open Data Portal](https://data.gov.ma/) | Published datasets and metadata | Homepage returned HTTP 403. The [official FAQ](https://data.gov.ma/index.php/fr/faq) describes ODbL for datasets and databases. Inspect the license and attribution requirements on the exact resource before reuse. |

## Phase 1 manual collection protocol

1. Open an official record and verify its publisher, reference, access conditions, permitted local use and redistribution rights. Record the URL and date of the terms or permission. If rights are unclear, defer inclusion until clarified.
2. Start with a few manually obtainable tender packages. Include native text and a scanned sample where available, with French and Arabic coverage. Store original bytes privately and log the original filename, MIME type, file size and SHA-256.
3. Record tender reference, issuer, category, publication date, submission deadline, original time-zone context, source URL, download timestamp and any amendment or version relationship. Use null for unknown fields and preserve the original date wording for review.
4. Deduplicate exact bytes by digest while keeping links between the document, source and relevant tender revisions. Treat amendments as separate versions. Keep a corpus manifest describing language, scan quality and permissions.
5. Publish a provenance inventory and reusable fixtures only when redistribution is allowed. Mark synthetic company profiles and documents clearly and keep them distinct from official records.

Only automate access after confirming the source permits the specific collection method. Honor restrictions, rate limits, and access requirements. Stop on CAPTCHA or authentication restrictions. Store private or permission-limited data outside the synchronized repository.
