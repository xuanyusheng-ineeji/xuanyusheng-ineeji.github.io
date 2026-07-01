---
permalink: /projects/
title: "Projects"
excerpt: ""
author_profile: true
---

<span class='anchor' id='projects'></span>

# 🏢 Industry Projects

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ineeji · 2025</div><img src='/images/data_collector_arch.png' alt="Data Collector Architecture" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Data Collector — Automated Financial & Energy Data Pipeline**

ineeji Co., Ltd. · AI Research Lab &nbsp;\|&nbsp; [**GitHub**](https://github.com/xuanyusheng-ineeji/data_collector)

An enterprise-grade automated pipeline that collects financial market data, commodity prices, and economic indicators from **20+ international sources** into Google Cloud Storage and BigQuery, with metadata governance via Google Data Catalog.

- **Data Sources**: EODHD, KOMIS/LME, Westmetall, IMF (financial); EIA, GIE (energy); FRED, BLS, OECD, World Bank, China NBS (economic); BOK, KOSIS, KMA, Chilean Customs, Port Hedland (regional); CFTC, Google Trends, MySteelNet, Gold.org (specialized)
- **Scheduler**: APScheduler with weekday 07:00/09:00, Friday 22:00 (weekly), monthly, and weekend triggers; automatic retry on data gaps
- **Storage**: Hive-partitioned CSVs on GCS (`fin_data/{table}/name={series}/dt={date}/data.csv`), exposed as BigQuery external tables; MySQL available as on-premise alternative
- **Governance**: Google Data Catalog for metadata management and dataset discovery
- **Tech**: `Python` · `APScheduler` · `GCS` · `BigQuery` · `Data Catalog` · `pandas` · `pyarrow` · `Selenium` · `pdfplumber` · `SQLAlchemy`

</div>
</div>

# 💡 Personal Projects

- **Project Name**, Brief description. \| [GitHub](https://github.com/xuanyusheng-ineeji)
