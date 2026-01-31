---
category: technology
date: '2023-07-29'
growthIcon: 🌿
tags: []
title: DocumentDB
---

#aws #NoSQL #database



# AWS DocumentDB

### [DocumentDB vs DynamoDB](https://cloud.netapp.com/blog/aws-cvo-blg-amazon-documentdb-basics-and-best-practices#H_H3)

> DocumentDB and DynamoDB are both services that you can use as  document databases. Both provide data portability and support migration  through the [AWS Database Migration Service](https://cloud.netapp.com/blog/aws-cvo-blg-aws-database-migration-service-copy-paste-your-database-to-amazon). Both services also provide encryption with AWS Key Management Service and auditing with CloudTrail, [CloudFormation](https://cloud.netapp.com/blog/infrastructure-as-code-on-aws-5-tips-to-get-you-started-cvo-blg), and VPC Flow Logs.
>
> Despite these similarities, the use cases for the two services differ slightly. DynamoDB is both a document database and a key-value  database. It is optimized for applications that rely on unique keys, but it is not as good at scan or query operations. **In contrast, DocumentDB  allows more flexible data indexing and is optimized for queries.**
>
> Another difference is the cost structure of the services. [DynamoDB pricing](https://cloud.netapp.com/blog/aws-cvo-blg-dynamodb-pricing-how-to-optimize-usage-and-reduce-costs) is according to read/write units with on-demand, provisioned, or  reserve pricing models. You can maintain small capacities to keep costs  low and the first 25GB of storage are free. 
>
> In contrast, DocumentDB is based on a pay per instance pricing model. The smallest available instance sizes are the r4.large or r5.large  instances. You can provision these instances or use bill per hour  pricing.

### [Impact of Indexes](https://cloud.netapp.com/blog/aws-cvo-blg-amazon-documentdb-basics-and-best-practices#H_H3)

> 

> Indexing enables you to decrease  query times by making it easier to locate the data you need. However,  when documents are indexed, each write or modification requires the  index to be updated. This means that write times increase according to  the number of indexes that must be updated each time. Indexes can also  increase I/O operations and storage use. 
>
> Minimizing the number of indexes you create, can help you speed query times without drastically affecting write times. In general, you are  recommended to use no more than five indexes per data collection.



### Change Stream

It's a way to monitor changes in a collection. It's a feature of MongoDB and other related databases. Might be useful for post processing write events (for example, an data anonymization step).

- [DocumentDB Change Stream](https://docs.aws.amazon.com/documentdb/latest/developerguide/change_streams.html)
- [MongoDB Change Stream](https://docs.mongodb.com/manual/changeStreams/)

### Python Library for using DocumentDB

[PyMongo](https://pymongo.readthedocs.io/en/stable/)

[AWS DocumentDB: Tutorial](https://aws.amazon.com/getting-started/hands-on/getting-started-amazon-documentdb-with-aws-cloud9/)

[AWS DocumentDB: Connecting Programmatically](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect_programmatically.html)



```python
import pymongo
import sys

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb://<sample-user>:<password>@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false') 

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()
```