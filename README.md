# Replicated Storage Systems

Distributed systems are the primary mechanism for implementing large scale applications that are highly available (respond to users in a timely fashion), particularly in today's mobile and web application environment where even small applications can receive hundreds of thousands of requests. Many developers are used to utilizing storage systems such as Amazon S3, MongoDB, or HDFS that were designed with the intent to be replicated storage to provide both durability and performance potentially across large geographic distances! However, the complexity of replicated storage means that very few developers have experience designing or implementing these types of systems.

There are extraordinary opportunities that exist now that challenge the assumption that traditional database systems will dominate in the long run. NoSQL databases have recently come into prominence by providing specific replication and data type solutions; graph databases, timeseries databases, key/value stores, document stores and even stores with per-cell security levels all provide multiple application opportunities for a variety of domains. Specialized file systems such as HDFS and S3 provide opportunities for geographic content hosting or Big Data computing. Finally programming languages such as Go, Scala, Erlang, and Rust are designed from the ground-up to support distributed communications and contexts. Although still not easy, now is an excellent time to dive into the creation of large scale distributed systems!

This book was created with the intent that I pass on some of the knowledge I gained by studying distributed systems in an academic context. My efforts were geared towards replicated file storage and consistency models -- but along the way I had to construct many different storage and replication protocols, and I've decided to document them here. Because I did my programming in Go, this book also serves as an introduction to building such systems in the Go programming language.

## Notes

This book is still under development and will continue to be as I get the time to fill in chapters. I've decided to create an open book format, which can be read online on [GitBook](https://www.gitbook.com/book/bbengfort/replicated-storage-systems/). The open format means a couple of things:

1. You can contribute! Submit [pull-requests](https://github.com/bbengfort/replicated-storage-systems/pulls) on GitHub.
2. You can [comment on and discuss](https://www.gitbook.com/book/bbengfort/replicated-storage-systems/discussions) the book as it's in progress!

This is meant to be a collaborative experiment, and will hopefully allow this book to be developed much faster; even if I do have to focus on my own implementations and research.

Finally, I'm currently licensing this book with a [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). That means you can copy and redistribute the material, even adapting it, so long as you attribute it correctly and share it yourself. I reserve the sole right to use this material for commercial purposes, however. If the time comes to develop this book into a commercial product, all your contributions and adaptations will be attributed in the book! 
