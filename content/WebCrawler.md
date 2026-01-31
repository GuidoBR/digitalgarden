---
category: technology
date: '2023-07-29'
growthIcon: 🪴
tags: []
title: WebCrawler
---

#system_design #programming #crawler

Definition from [Wikipedia](https://en.wikipedia.org/wiki/Web_crawler)

> A **Web crawler**, sometimes called a **spider** or **spiderbot** and often shortened to **crawler**, is an [Internet bot](https://en.wikipedia.org/wiki/Internet_bot) that systematically browses the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) and that is typically operated by search engines for the purpose of [Web indexing](https://en.wikipedia.org/wiki/Web_indexing) (*web spidering*).[[1\]](https://en.wikipedia.org/wiki/Web_crawler#cite_note-1)
>
> [Web search engines](https://en.wikipedia.org/wiki/Web_search_engine) and some other [websites](https://en.wikipedia.org/wiki/Website) use Web crawling or spidering [software](https://en.wikipedia.org/wiki/Software) to update their [web content](https://en.wikipedia.org/wiki/Web_content) or indices of other sites' web content. Web crawlers copy pages for processing by a search engine, which [indexes](https://en.wikipedia.org/wiki/Index_(search_engine)) the downloaded pages so that users can search more efficiently.
>
> Crawlers consume resources on visited systems and often visit  sites unprompted. Issues of schedule, load, and "politeness" come into  play when large collections of pages are accessed. Mechanisms exist for  public sites not wishing to be crawled to make this known to the  crawling agent. For example, including a `robots.txt` file can request [bots](https://en.wikipedia.org/wiki/Software_agent) to index only parts of a website, or nothing at all.



### Architecture

Shkapenyuk and Suel noted that:[[43\]](https://en.wikipedia.org/wiki/Web_crawler#cite_note-shkapenyuk2002-43)

> While it is fairly easy to build a  slow crawler that downloads a few pages per second for a short period of time, building a high-performance system that can download hundreds of  millions of pages over several weeks presents a number of challenges in  system design, I/O and network efficiency, and robustness and  manageability.



reference: [Design Web Crawler](https://roadtoarchitect.com/2019/04/01/design-web-crawler/)

<img data-attachment-id="74" data-permalink="https://roadtoarchitect.com/2019/04/01/design-web-crawler/download-3/" data-orig-file="https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png" data-orig-size="900,549" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="download" data-image-description="" data-image-caption="" data-medium-file="https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=300" data-large-file="https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=900" class="alignnone size-full wp-image-74" src="https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=1100" alt="download" srcset="https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png 900w, https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=150 150w, https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=300 300w, https://roadtoarchitectcom.files.wordpress.com/2019/03/download.png?w=768 768w" sizes="(max-width: 900px) 100vw, 900px">

**1. The URL frontier:** The URL frontier is the data  structure that contains all the URLs that remain to be downloaded. We  can crawl by performing a breadth-first traversal of the Web, starting  from the pages in the seed set. Such traversals are easily implemented  by using a FIFO queue.

**2. The fetcher module:** The purpose of a fetcher module  is to download the document corresponding to a given URL using the  appropriate network protocol like HTTP. As discussed above, webmasters  create robot.txt to make certain parts of their websites off limits for  the crawler. To avoid downloading this file on every request, our  crawler’s HTTP protocol module can maintain a fixed-sized cache mapping  host-names to their robot’s exclusion rules.

**3. Document input stream:** Our crawler’s design  enables the same document to be processed by multiple processing  modules. To avoid downloading a document multiple times, we cache the  document locally using an abstraction called a Document Input Stream  (DIS).

A DIS is an input stream that caches the entire contents of the  document read from the internet. It also provides methods to re-read the document. The DIS can cache small documents (64 KB or less) entirely in memory, while larger documents can be temporarily written to a backing  file.

Each worker thread has an associated DIS, which it reuses from  document to document. After extracting a URL from the frontier, the  worker passes that URL to the relevant protocol module, which  initializes the DIS from a network connection to contain the document’s  contents. The worker then passes the DIS to all relevant processing  modules.

**4. Document Dedupe test:** Many documents on the Web  are available under multiple, different URLs. There are also many cases  in which documents are mirrored on various servers. Both of these  effects will cause any Web crawler to download the same document  multiple times. To prevent processing of a document more than once, we  perform a dedupe test on each document to remove duplication.

To perform this test, we can calculate a 64-bit checksum of every  processed document and store it in a database. For every new document,  we can compare its checksum to all the previously calculated checksums  to see the document has been seen before. We can use MD5 or SHA to  calculate these checksums.

**5. URL filters:** The URL filtering mechanism provides a customizable way to control the set of URLs that are downloaded. This is used to blacklist websites so that our crawler can ignore them.  Before adding each URL to the frontier, the worker thread consults the  user-supplied URL filter. We can define filters to restrict URLs by  domain, prefix, or protocol type.

**6. Domain name resolution:** Before contacting a Web  server, a Web crawler must use the Domain Name Service (DNS) to map the  Web server’s hostname into an IP address. DNS name resolution will be a  big bottleneck of our crawlers given the amount of URLs we will be  working with. To avoid repeated requests, we can start caching DNS  results by building our local DNS server.

**7. URL dedupe test:** While extracting links, any Web  crawler will encounter multiple links to the same document. To avoid  downloading and processing a document multiple times, a URL dedupe test  must be performed on each extracted link before adding it to the URL  frontier.

To perform the URL dedupe test, we can store all the URLs seen by our crawler in canonical form in a database. To save space, we do not store the textual representation of each URL in the URL set, but rather a  fixed-sized checksum.

To reduce the number of operations on the database store, we can keep an in-memory cache of popular URLs on each host shared by all threads.  The reason to have this cache is that links to some URLs are quite  common, so caching the popular ones in memory will lead to a high  in-memory hit rate.





### Tools

- [Scrapy](https://scrapy.org/)