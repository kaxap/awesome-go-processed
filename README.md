this is a processed copy of https://raw.githubusercontent.com/avelino/awesome-go/master/README.md

# Awesome Go [![Build Status](https://travis-ci.org/avelino/awesome-go.svg?branch=master)](https://travis-ci.org/avelino/awesome-go) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Join the chat at https://gitter.im/avelino/awesome-go](https://badges.gitter.im/avelino/awesome-go.svg)](https://gitter.im/avelino/awesome-go?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A curated list of awesome Go frameworks, libraries and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python).

### Contributing

Please take a quick gander at the [contribution guidelines](https://github.com/avelino/awesome-go/blob/master/CONTRIBUTING.md) first. Thanks to all [contributors](https://github.com/avelino/awesome-go/graphs/contributors); you rock!

#### *If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you!*

### Contents

- [Awesome Go](#awesome-go)
    - [Audio and Music](#audio-and-music)
    - [Authentication and OAuth](#authentication-and-oauth)
    - [Command Line](#command-line)
    - [Configuration](#configuration)
    - [Continuous Integration](#continuous-integration)
    - [CSS Preprocessors](#css-preprocessors)
    - [Data Structures](#data-structures)
    - [Database](#database)
    - [Database Drivers](#database-drivers)
    - [Date and Time](#date-and-time)
    - [Distributed Systems](#distributed-systems)
    - [Email](#email)
    - [Embeddable Scripting Languages](#embeddable-scripting-languages)
    - [Files](#files)
    - [Financial](#financial)
    - [Forms](#forms)
    - [Game Development](#game-development)
    - [Generation and Generics](#generation-and-generics)
    - [Go Compilers](#go-compilers)
    - [Goroutines](#goroutines)
    - [GUI](#gui)
    - [Hardware](#hardware)
    - [Images](#images)
    - [IoT](#iot-internet-of-things)
    - [Logging](#logging)
    - [Machine Learning](#machine-learning)
    - [Messaging](#messaging)
    - [Miscellaneous](#miscellaneous)
    - [Natural Language Processing](#natural-language-processing)
    - [Networking](#networking)
    - [OpenGL](#opengl)
    - [ORM](#orm)
    - [Package Management](#package-management)
    - [Query Language](#query-language)
    - [Resource Embedding](#resource-embedding)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Security](#security)
    - [Serialization](#serialization)
    - [Template Engines](#template-engines)
    - [Testing](#testing)
    - [Text Processing](#text-processing)
    - [Third-party APIs](#third-party-apis)
    - [Utilities](#utilities)
    - [Validation](#validation)
    - [Version Control](#version-control)
    - [Video](#video)
    - [Web Frameworks](#web-frameworks)
        - [Middlewares](#middlewares)
            - [Actual middlewares](#actual-middlewares)
            - [Libraries for creating HTTP middlewares](#libraries-for-creating-http-middlewares)
        - [Routers](#routers)
    - [Windows](#windows)
    - [XML](#xml)

- [Tools](#tools)
    - [Code Analysis](#code-analysis)
    - [Editor Plugins](#editor-plugins)
    - [Go Tools](#go-tools)
    - [Software Packages](#software-packages)
        - [DevOps Tools](#devops-tools)
        - [Other Software](#other-software)

- [Server Applications](#server-applications)

- [Resources](#resources)
    - [Benchmarks](#benchmarks)
    - [Conferences](#conferences)
    - [E-Books](#e-books)
    - [Twitter](#twitter)
    - [Websites](#websites)
        - [Tutorials](#tutorials)

## Audio and Music

*Libraries for manipulating audio.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|189|10|2|* [waveform](https://github.com/mdlayher/waveform) - Go package capable of generating waveform images from audio streams.|
|168|16|6|* [music-theory](https://github.com/go-music-theory/music-theory) - Music theory models in Go.|
|149|31|2|* [PortAudio](https://github.com/gordonklaus/portaudio) - Go bindings for the PortAudio audio I/O library.|
|137|38|10|* [portmidi](https://github.com/rakyll/portmidi) - Go bindings for PortMidi.|
|71|7|2|* [flac](https://github.com/eaburns/flac) - Native Go FLAC decoder.|
|63|11|11|* [mix](https://github.com/go-mix/mix) - Sequence-based Go-native audio mixer for music apps.|
|59|7|0|* [mp3](https://github.com/tcolgate/mp3) - Native Go MP3 decoder.|
|52|16|3|* [taglib](https://github.com/wtolson/go-taglib) - Go bindings for taglib.|
|51|12|2|* [flac](https://github.com/mewkiz/flac) - Native Go FLAC decoder.|
|50|8|5|* [go-sox](https://github.com/krig/go-sox) - libsox bindings for go.|
|48|7|2|* [id3v2](https://github.com/bogem/id3v2) - Fast and stable ID3 parsing and writing library for Go.|
|30|2|1|* [gaad](https://github.com/Comcast/gaad) - Native Go AAC bitstream parser.|
|16|5|2|* [vorbis](https://github.com/mccoyst/vorbis) - "Native" Go Vorbis decoder (uses CGO, but has no dependencies).|
|16|4|0|* [go_mediainfo](https://github.com/zhulik/go_mediainfo) - libmediainfo bindings for go.|
|3|0|0|* [gosamplerate](https://github.com/dh1tw/gosamplerate) - libsamplerate bindings for go.|

*Libraries for implementing authentications schemes.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|9547|890|304|* [traefik](https://github.com/containous/traefik) - Reverse proxy and load balancer with support for multiple backends.|
|2492|274|37|* [jwt-go](https://github.com/dgrijalva/jwt-go) - Golang implementation of JSON Web Tokens (JWT).|
|1305|153|20|* [goth](https://github.com/markbates/goth) - provides a simple, clean, and idiomatic way to use OAuth and OAuth2. Handles multiple provides out of the box.|
|1242|318|40|* [oauth2](https://github.com/golang/oauth2) - Successor of goauth2. Generic OAuth 2.0 package that comes with JWT, Google APIs, Compute Engine and App Engine support.|
|1219|248|31|* [osin](https://github.com/RangelReale/osin) - Golang OAuth2 server library.|
|1182|83|35|* [authboss](https://github.com/volatiletech/authboss) - Modular authentication system for the web. It tries to remove as much boilerplate and "hard things" as possible so that each time you start a new web project in Go, you can plug it in, configure, and start building your app without having to build an authentication system each time.|
|1134|123|4|* [casbin](https://github.com/hsluoyz/casbin) - Authorization library that supports access control models like ACL, RBAC, ABAC.|
|769|37|2|* [gologin](https://github.com/dghubble/gologin) - chainable handlers for login with OAuth1 and OAuth2 authentication providers.|
|726|93|16|* [go-jose](https://github.com/square/go-jose) - Fairly complete implementation of the JOSE working group's JSON Web Token, JSON Web Signatures, and JSON Web Encryption specs.|
|618|71|5|* [go-oauth2-server](https://github.com/RichardKnop/go-oauth2-server) - Standalone, specification-compliant,  OAuth2 server written in Golang.|
|596|100|1|* [gorbac](https://github.com/mikespook/gorbac) - provides a lightweight role-based access control (RBAC) implementation in Golang.|
|442|25|11|* [loginsrv](https://github.com/tarent/loginsrv) - JWT login microservice with plugable backends such as OAuth2 (Github), htpasswd, osiam.|
|347|30|9|* [go.auth](https://github.com/bradrydzewski/go.auth) - Authentication API for Go web applications.|
|237|13|2|* [permissions2](https://github.com/xyproto/permissions2) - Library for keeping track of users, login states and permissions. Uses secure cookies and bcrypt.|
|174|38|17|* [Go-AWS-Auth](https://github.com/smartystreets/go-aws-auth) - AWS (Amazon Web Services) request signing library.|
|120|16|1|* [httpauth](https://github.com/goji/httpauth) - HTTP Authentication middleware.|
|75|10|3|* [yubigo](https://github.com/GeertJohan/yubigo) - Yubikey client package that provides a simple API to integrate the Yubico Yubikey into a go application.|
|75|6|0|* [jwt-auth](https://github.com/adam-hanna/jwt-auth) - JWT middleware for goLang http servers with many configuration options.|
|37|3|3|* [session](https://github.com/icza/session) - Go session management for web servers (including support for Google App Engine - GAE).|
|23|0|1|* [sessions](https://github.com/adam-hanna/sessions) - Dead simple, highly performant, highly customizable sessions service for go http servers.|
|20|6|7|* [jwt](https://github.com/robbert229/jwt) - Clean and easy to use implementation of JSON Web Tokens (JWT).|

### Standard CLI

*Libraries for building standard or basic Command Line applications.*

* [climax](http://github.com/tucnak/climax) - Alternative CLI with "human face", in spirit of Go command.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|6414|593|77|* [urfave/cli](https://github.com/urfave/cli) - Simple, fast, and fun package for building command line apps in Go (formerly codegangsta/cli).|
|5062|419|77|* [cobra](https://github.com/spf13/cobra) - Commander for modern Go CLI interactions.|
|3460|275|167|* [drive](https://github.com/odeke-em/drive) - Google Drive client for the commandline.|
|1431|97|11|* [kingpin](https://github.com/alecthomas/kingpin) - Command line and flag parser supporting sub commands.|
|873|117|14|* [go-flags](https://github.com/jessevdk/go-flags) - go command line option parser.|
|859|75|38|* [readline](https://github.com/chzyer/readline) - Pure golang implementation that provide most of features in GNU-Readline under MIT license.|
|852|69|23|* [docopt.go](https://github.com/docopt/docopt.go) - Command-line arguments parser that will make you smile.|
|735|63|18|* [cli-init](https://github.com/tcnksm/gcli) - The easy way to start building Golang command line application.|
|663|53|8|* [mitchellh/cli](https://github.com/mitchellh/cli) - Go library for implementing command-line interfaces.|
|425|19|1|* [go-arg](https://github.com/alexflint/go-arg) - Struct-based argument parsing in Go.|
|423|27|5|* [mow.cli](https://github.com/jawher/mow.cli) - Go library for building CLI applications with sophisticated flag and argument parsing and validation.|
|390|63|2|* [liner](https://github.com/peterh/liner) - Go readline-like library for command-line interfaces.|
|300|25|11|* [cli](https://github.com/mkideal/cli) - Feature-rich and easy to use command-line package based on golang tag.|
|238|85|11|* [pflag](https://github.com/spf13/pflag) - Drop-in replacement for Go's flag package, implementing POSIX/GNU-style --flags.|
|197|8|3|* [complete](https://github.com/posener/complete) - Write bash completions in Go + Go command bash completion.|
|77|8|5|* [ukautz/clif](https://github.com/ukautz/clif) - Small command line interface framework.|
|70|2|3|* [flag](https://github.com/cosiner/flag) - Simple but powerful command line option parsing library for Go support subcommand.|
|44|3|3|* [sflags](https://github.com/octago/sflags) - Struct based flags generator for flag, urfave/cli, pflag, cobra, kingpin and other libraries.|
|34|4|1|* [wmenu](https://github.com/dixonwille/wmenu) - Easy to use menu structure for cli applications that prompts users to make choices.|
|19|2|0|* [wlog](https://github.com/dixonwille/wlog) - Simple logging interface that supports cross-platform color and concurrency.|
|5|0|0|* [env](https://github.com/codingconcepts/env) - Tag-based environment configuration for structs.|
|2|0|0|* [argv](https://github.com/cosiner/argv) - Go library to split command line string as arguments array using the bash syntax.|

*Libraries for building Console Applications and Console User Interfaces.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|6397|353|69|* [termui](https://github.com/gizak/termui) - Go terminal dashboard based on **termbox-go** and inspired by [blessed-contrib](https://github.com/yaronn/blessed-contrib).|
|2340|206|38|* [termbox-go](https://github.com/nsf/termbox-go) - Termbox is a library for creating cross-platform text-based interfaces.|
|1880|120|7|* [gocui](https://github.com/jroimartin/gocui) - Minimalist Go library aimed at creating Console User Interfaces.|
|1794|139|4|* [color](https://github.com/fatih/color) - Versatile package for colored terminal output.|
|983|47|10|* [uiprogress](https://github.com/gosuri/uiprogress) - Flexible library to render progress bars in terminal applications.|
|565|23|10|* [uilive](https://github.com/gosuri/uilive) - Library for updating terminal output in realtime.|
|387|13|2|* [uitable](https://github.com/gosuri/uitable) - Library to improve readability in terminal apps using tabular data.|
|243|7|0|* [aurora](https://github.com/logrusorgru/aurora) - ANSI terminal colors that supports fmt.Printf/Sprintf.|
|208|13|2|* [chalk](https://github.com/ttacon/chalk) - Intuitive package for prettifying terminal/console output.|
|200|32|3|* [go-colorable](https://github.com/mattn/go-colorable) - Colorable writer for windows.|
|171|20|0|* [go-isatty](https://github.com/mattn/go-isatty) - isatty for golang.|
|160|10|2|* [go-colortext](https://github.com/daviddengcn/go-colortext) - Go library for color output in terminals.|
|101|14|6|* [termtables](https://github.com/apcera/termtables) - Go port of the Ruby library [terminal-tables](https://github.com/tj/terminal-table) for simple ASCII table generation as well as providing markdown and HTML output.|
|94|9|1|* [mpb](https://github.com/vbauerster/mpb) - Multi progress bar for terminal applications.|
|11|2|0|* [colourize](https://github.com/TreyBastian/colourize) - Go library for ANSI colour text in terminals.|
|1|0|0|* [go-ataman](https://github.com/workanator/go-ataman) - Go library for rendering ANSI colored text templates in terminals.|
|0|0|0|* [gommon/color](https://github.com/labstack/gommon/tree/master/color) - Style terminal text.|

*Libraries for configuration parsing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3586|372|143|* [viper](https://github.com/spf13/viper) - Go configuration with fangs.|
|662|45|10|* [godotenv](https://github.com/joho/godotenv) - Go port of Ruby's dotenv library (Loads environment variables from `.env`).|
|653|123|9|* [ini](https://github.com/go-ini/ini) - Go package for read and write INI files.|
|303|28|1|* [env](https://github.com/caarlos0/env) - Parse environment variables to Go structs (with defaults).|
|207|9|0|* [store](https://github.com/tucnak/store) - Lightweight configuration manager for Go.|
|142|7|1|* [joshbetz/config](https://github.com/joshbetz/config) - Small configuration library for Go that parses environment variables, JSON files, and reloads automatically on SIGHUP.|
|123|23|2|* [config](https://github.com/olebedev/config) - JSON or YAML configuration wrapper with environment variables and flags parsing.|
|108|9|1|* [envconfig](https://github.com/vrischmann/envconfig) - Read your configuration from environment variables.|
|93|9|0|* [hjson](https://github.com/hjson/hjson-go) - Human JSON, a configuration file format for humans. Relaxed syntax, fewer mistakes, more comments.|
|81|5|0|* [envcfg](https://github.com/tomazk/envcfg) - Un-marshaling environment variables to Go structs.|
|67|17|3|* [gcfg](https://github.com/go-gcfg/gcfg) - read INI-style configuration files into Go structs; supports user-defined types and subsections.|
|44|6|0|* [gofigure](https://github.com/ian-kent/gofigure) - Go application configuration made easy.|
|43|9|3|* [goConfig](https://github.com/crgimenes/goConfig) - Parse a struct as input and populates the fields of this struct with parameters fom command line, environment variables and configuration file.|
|28|3|0|* [configure](https://github.com/paked/configure) - Provides configuration through multiple sources, including JSON, flags and environment variables.|
|13|1|0|* [ingo](https://github.com/schachmat/ingo) - Flags persisted in an ini-like config file.|
|12|4|0|* [mini](https://github.com/sasbury/mini) - Golang package for parsing ini-style configuration files.|
|5|2|0|* [envconf](https://github.com/ian-kent/envconf) - Configuration from environment.|
|0|0|0|* [xdg](https://github.com/OpenPeeDeeP/xdg) - Cross platform package that follows the [XDG Standard](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html).|
|0|0|0|* [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) - Modular JSON configuration. Keep you config structs along the code they configure and delegate parsing to submodules without sacrificing full config serialization.|

*Tools for help with continuous integration.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|10906|1232|109|* [drone](https://github.com/drone/drone) - Drone is a Continuous Integration platform built on Docker, written in Go.|
|410|65|9|* [goveralls](https://github.com/mattn/goveralls) - Go integration for Coveralls.io continuous code coverage tracking system.|
|65|16|1|* [overalls](https://github.com/go-playground/overalls) - Multi-Package go project coverprofile for tools like goveralls.|
|1|0|0|* [roveralls](https://github.com/LawrenceWoodman/roveralls) - Recursive coverage testing tool.|

*Libraries for preprocessing CSS files.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|384|24|7|* [gcss](https://github.com/yosssi/gcss) - Pure Go CSS Preprocessor.|
|379|24|47|* [c6](https://github.com/c9s/c6) - High performance SASS compatible-implementation compiler written in Go.|
|60|8|9|* [go-libsass](https://github.com/wellington/go-libsass) - Go wrapper to the 100% Sass compatible libsass project.|

*Generic datastructures and algorithms in Go.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3389|333|8|* [go-datastructures](https://github.com/Workiva/go-datastructures) - Collection of useful, performant, and thread-safe data structures.|
|3107|270|9|* [gods](https://github.com/emirpasic/gods) - Go Data Structures. Containers, Sets, Lists, Stacks, Maps, BidiMaps, Trees, HashSet etc.|
|845|50|5|* [boomfilters](https://github.com/tylertreat/BoomFilters) - Probabilistic data structures for processing continuous, unbounded streams.|
|592|74|4|* [golang-set](https://github.com/deckarep/golang-set) - Thread-Safe and Non-Thread-Safe high-performance sets for Go.|
|545|17|0|* [hyperloglog](https://github.com/axiomhq/hyperloglog) - HyperLogLog implementation with Sparse, LogLog-Beta bias correction and TailCut space reduction.|
|351|64|2|* [willf/bloom](https://github.com/willf/bloom) - Go package implementing Bloom filters.|
|311|36|10|* [gota](https://github.com/kniren/gota) - Implementation of dataframes, series, and data wrangling methods for Go.|
|303|62|0|* [bitset](https://github.com/willf/bitset) - Go package implementing bitsets.|
|274|33|21|* [roaring](https://github.com/RoaringBitmap/roaring) - Go package implementing compressed bitsets.|
|258|32|2|* [go-geoindex](https://github.com/hailocab/go-geoindex) - In-memory geo index.|
|254|17|8|* [mafsa](https://github.com/smartystreets/mafsa) - MA-FSA implementation with Minimal Perfect Hashing.|
|235|17|2|* [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - Cuckoo filter: a good alternative to a counting bloom filter implemented in Go.|
|198|21|5|* [trie](https://github.com/derekparker/trie) - Trie implementation in Go.|
|136|30|1|* [goskiplist](https://github.com/ryszard/goskiplist) - Skip list implementation in Go.|
|103|10|0|* [bloom](https://github.com/zhenjl/bloom) - Bloom filters implemented in Go.|
|94|11|2|* [hilbert](https://github.com/google/hilbert) - Go package for mapping values to and from space-filling curves, such as Hilbert and Peano curves.|
|74|9|1|* [encoding](https://github.com/zhenjl/encoding) - Integer Compression Libraries for Go.|
|71|2|1|* [go-rquad](https://github.com/aurelien-rainone/go-rquad) - Region quadtrees with efficient point location and neighbour finding.|
|50|11|0|* [binpacker](https://github.com/zhuangsirui/binpacker) - Binary packer and unpacker helps user build custom binary stream.|
|45|5|1|* [ttlcache](https://github.com/diegobernardes/ttlcache) - In-memory LRU string-interface{} map with expiration for golang.|
|40|8|1|* [skiplist](https://github.com/gansidui/skiplist) - Skiplist implementation in Go.|
|32|4|0|* [count-min-log](https://github.com/seiflotfy/count-min-log) - Go implementation Count-Min-Log sketch: Approximately counting with approximate counters (Like Count-Min sketch but using less memory).|
|21|4|0|* [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - Go implementation of Adaptive Radix Tree.|
|9|1|0|* [levenshtein](https://github.com/agnivade/levenshtein) - Implementation to calculate levenshtein distance in Go.|
|7|0|0|* [merkletree](https://github.com/cbergoon/merkletree) - Implementation of a merkle tree providing an efficient and secure verification of the contents of data structures.|
|6|0|0|* [levenshtein](https://github.com/agext/levenshtein) - Levenshtein distance and similarity metrics with customizable edit costs and Winkler-like bonus for common prefix.|
|4|1|0|* [bit](https://github.com/yourbasic/bit) - Golang set data structure with bonus bit-twiddling functions.|
|4|1|0|* [goset](https://github.com/zoumo/goset) - A useful Set collection implementation for Go.|
|2|0|0|* [bloom](https://github.com/yourbasic/bloom) - Golang Bloom filter implementation.|

*Databases implemented in Go.*


*Database schema migration.*


*Database tools.*


*SQL query builder, libraries for building and using SQL.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|11396|1625|557|* [influxdb](https://github.com/influxdb/influxdb) - Scalable datastore for metrics, events, and real-time analytics.|
|11392|1285|227|* [prometheus](https://github.com/prometheus/prometheus) - Monitoring system and time series database.|
|10972|1098|1050|* [cockroach](https://github.com/cockroachdb/cockroach) - Scalable, Geo-Replicated, Transactional Datastore.|
|9370|1288|341|* [tidb](https://github.com/pingcap/tidb) - TiDB is a distributed SQL database. Inspired by the design of Google F1.|
|6804|553|107|* [bolt](https://github.com/boltdb/bolt) - Low-level key/value database for Go.|
|5713|663|10|* [groupcache](https://github.com/golang/groupcache) - Groupcache is a caching and cache-filling library, intended as a replacement for memcached in many cases.|
|4929|645|110|* [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.|
|4466|286|21|* [pgweb](https://github.com/sosedoff/pgweb) - Web-based PostgreSQL database browser.|
|3692|189|64|* [dgraph](https://github.com/dgraph-io/dgraph) - Scalable, Distributed, Low Latency, High Throughput Graph Database.|
|3338|156|42|* [Tile38](https://github.com/tidwall/tile38) - Geolocation DB with spatial index and realtime geofencing.|
|3140|154|30|* [rqlite](https://github.com/rqlite/rqlite) - The lightweight, distributed, relational database built on SQLite.|
|2884|589|43|* [kingshard](https://github.com/flike/kingshard) - kingshard is a high performance proxy for MySQL powered by Golang.|
|2223|262|83|* [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb is a high performance NoSQL like Redis based on LevelDB.|
|1896|169|14|* [tiedot](https://github.com/HouzuoGuo/tiedot) - Your NoSQL database powered by Golang.|
|1740|224|24|* [goleveldb](https://github.com/syndtr/goleveldb) - Implementation of the [LevelDB](https://github.com/google/leveldb) key/value database in the Go.|
|1563|97|2|* [buntdb](https://github.com/tidwall/buntdb) - Fast, embeddable, in-memory key/value database for Go with custom indexing and spatial support.|
|1527|252|42|* [migrate](https://github.com/mattes/migrate) - Database migrations. CLI and Golang library.|
|1408|45|22|* [pREST](https://github.com/nuveo/prest) - Serve a RESTful API from any PostgreSQL database.|
|1243|102|41|* [xo](https://github.com/knq/xo) - Generate idiomatic Go code for databases based on existing schema definitions or custom queries supporting PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server.|
|1195|98|32|* [Squirrel](https://github.com/Masterminds/squirrel) - Go library that helps you build SQL queries.|
|1062|195|27|* [go-cache](https://github.com/pmylund/go-cache) - In-memory key:value store/cache (similar to Memcached) library for Go, suitable for single-machine applications.|
|1048|73|3|* [BigCache](https://github.com/allegro/bigcache) - Efficient key/value cache for gigabytes of data.|
|856|202|52|* [go-mysql-elasticsearch](https://github.com/siddontang/go-mysql-elasticsearch) - Sync your MySQL data into Elasticsearch automatically.|
|840|113|61|* [orchestrator](https://github.com/github/orchestrator) - MySQL replication topology manager & visualizer.|
|743|78|31|* [sql-migrate](https://github.com/rubenv/sql-migrate) - Database migration tool. Allows embedding migrations into the application using go-bindata.|
|633|166|20|* [go-mysql](https://github.com/siddontang/go-mysql) - Go toolset to handle MySQL protocol and replication.|
|475|46|2|* [diskv](https://github.com/peterbourgon/diskv) - Home-grown disk-backed key-value store.|
|456|38|25|* [dat](https://github.com/mgutz/dat) - Go Postgres Data Access Toolkit.|
|431|15|2|* [eliasdb](https://github.com/krotik/eliasdb) - Dependency-free, transactional graph database with REST API, phrase search and SQL-like query language.|
|346|23|36|* [moss](https://github.com/couchbase/moss) - Moss is a simple LSM key-value storage engine written in 100% Go.|
|334|33|9|* [goqu](https://github.com/doug-martin/goqu) - Idiomatic SQL builder and query library.|
|312|129|0|* [cache2go](https://github.com/muesli/cache2go) - In-memory key:value cache which supports automatic invalidation based on timeouts.|
|306|63|3|* [levigo](https://github.com/jmhodges/levigo) - Levigo is a Go wrapper for LevelDB.|
|306|19|2|* [Dotsql](https://github.com/gchaincl/dotsql) - Go library that helps you keep sql files in one place and use it with ease.|
|233|31|8|* [GCache](https://github.com/bluele/gcache) - Cache library with support for expirable Cache, LFU, LRU and ARC.|
|174|24|5|* [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - Powerful data retrieval methods as well as DB-agnostic query building capabilities.|
|139|14|11|* [piladb](https://github.com/fern4lvarez/piladb) - Lightweight RESTful database engine based on stack data structures.|
|109|8|3|* [scaneo](https://github.com/variadico/scaneo) - Generate Go code to convert database rows into arbitrary structs.|
|82|28|3|* [myreplication](https://github.com/2tvenom/myreplication) - MySql binary log replication listener. Support statement and row based replication.|
|79|6|1|* [sqrl](https://github.com/elgris/sqrl) - SQL query builder, fork of Squirrel with improved performance.|
|70|19|5|* [Scribble](https://github.com/nanobox-io/golang-scribble) - Tiny flat file JSON store.|
|68|2|0|* [geocache](https://github.com/melihmucuk/geocache) - In-memory cache that is suitable for geolocation based applications.|
|61|2|0|* [igor](https://github.com/galeone/igor) - Abstraction layer for PostgreSQL that supports advanced functionality and uses gorm-like syntax.|
|60|6|0|* [gormigrate](https://github.com/go-gormigrate/gormigrate) - Database schema migration helper for Gorm ORM.|
|48|7|5|* [goose](https://github.com/steinbacher/goose) - Database migration tool. You can manage your database's evolution by creating incremental SQL or Go scripts.|
|42|4|0|* [darwin](https://github.com/GuiaBolso/darwin) - Database schema evolution library for Go.|
|27|3|7|* [forestdb](https://github.com/couchbase/goforestdb) - Go bindings for ForestDB.|
|25|2|0|* [couchcache](https://github.com/codingsince1985/couchcache) - RESTful caching micro-service backed by Couchbase server.|
|18|3|30|* [pravasan](https://github.com/pravasan/pravasan) - Simple Migration tool - currently for MySQL but planning to support soon for Postgres, SQLite, MongoDB, etc.|
|6|1|0|* [tempdb](https://github.com/rafaeljesus/tempdb) - Key-value store for temporary items.|
|2|3|0|* [go-fixtures](https://github.com/RichardKnop/go-fixtures) - Django style fixtures for Golang's excellent built-in database/sql library.|
|0|0|0|* [soda](https://github.com/markbates/pop/tree/master/soda) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.|

*Libraries for connecting and operating databases.*

* Relational Databases

* NoSQL Databases
    * [gocql](http://gocql.github.io) - Go language driver for Apache Cassandra.
    * [mgo](https://godoc.org/labix.org/v2/mgo) - MongoDB driver for the Go language that implements a rich and well tested selection of features under a very simple API following standard Go idioms.

* Search and Analytic Databases.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|10421|899|65|    * [cayley](https://github.com/google/cayley) - Graph database with support for multiple backends.|
|4076|882|61|    * [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - MySQL driver for Go.|
|3472|584|7|    * [redigo](https://github.com/garyburd/redigo) - Redigo is a Go client for the Redis database.|
|3460|298|93|    * [bleve](https://github.com/blevesearch/bleve) - Modern text indexing library for go.|
|3133|427|122|    * [pq](https://github.com/lib/pq) - Pure Go Postgres driver for database/sql.|
|2200|345|15|    * [redis](https://github.com/go-redis/redis) - Redis client for Golang.|
|1964|448|68|    * [go-sqlite3](https://github.com/mattn/go-sqlite3) - SQLite3 driver for go that using database/sql.|
|1633|378|25|    * [elastic](https://github.com/olivere/elastic) - Elasticsearch client for Go.|
|1217|133|8|    * [gorethink](https://github.com/dancannon/gorethink) - Go language driver for RethinkDB.|
|1094|124|35|    * [pgx](https://github.com/jackc/pgx) - PostgreSQL driver supporting features beyond those exposed by database/sql.|
|875|241|75|    * [elastigo](https://github.com/mattbaird/elastigo) - Elasticsearch client library.|
|588|121|50|    * [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - Microsoft MSSQL driver for Go.|
|536|192|19|    * [redis](https://github.com/hoisie/redis) - Simple, powerful Redis client for Go.|
|304|50|14|    * [neoism](https://github.com/jmcvetta/neoism) - Neo4j client for Golang.|
|246|78|31|    * [go-couchbase](https://github.com/couchbase/go-couchbase) - Couchbase client in Go.|
|230|93|10|    * [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Aerospike client in Go language.|
|228|131|52|    * [go-oci8](https://github.com/mattn/go-oci8) - Oracle driver for go that using database/sql.|
|223|58|0|    * [gocb](https://github.com/couchbase/gocb) - Official Couchbase Go SDK.|
|141|15|0|    * [redis](https://github.com/bsm/redeo) - Redis-protocol compatible TCP servers/services.|
|130|14|5|    * [go-bqstreamer](https://github.com/rounds/go-bqstreamer) - BigQuery fast and concurrent stream insert.|
|95|14|4|    * [elasticsql](https://github.com/cch123/elasticsql) - Convert sql to elasticsearch dsl in Go.|
|75|30|5|    * [goes](https://github.com/belogik/goes) - Library to interact with Elasticsearch.|
|65|14|1|    * [Neo4j-GO](https://github.com/davemeehan/Neo4j-GO) - Neo4j REST Client in golang.|
|64|15|9|    * [firebirdsql](https://github.com/nakagami/firebirdsql) - Firebird RDBMS SQL driver for Go.|
|59|25|10|    * [go-adodb](https://github.com/mattn/go-adodb) - Microsoft ActiveX Object DataBase driver for go that using database/sql.|
|50|14|3|    * [arangolite](https://github.com/solher/arangolite) - Lightweight golang driver for ArangoDB.|
|50|25|10|    * [gofreetds](https://github.com/minus5/gofreetds) - Microsoft MSSQL driver. Go wrapper over [FreeTDS](http://www.freetds.org).|
|45|22|16|    * [go-couchdb](https://github.com/fjl/go-couchdb) - Yet another CouchDB HTTP API wrapper for Go.|
|45|11|1|    * [dynago](https://github.com/underarmour/dynago) - Dynago is a principle of least surprise client for DynamoDB.|
|45|7|0|    * [skizze](https://github.com/seiflotfy/skizze) - probabilistic data-structures service and storage.|
|32|7|0|    * [avatica](https://github.com/Boostport/avatica) - Apache Phoenix/Avatica SQL driver for database/sql.|
|22|3|8|    * [neo4j](https://github.com/cihangir/neo4j) - Neo4j Rest API Bindings for Golang.|
|18|2|3|    * [goriak](https://github.com/zegl/goriak) - Go language driver for Riak KV.|
|6|1|0|    * [xredis](https://github.com/shomali11/xredis) - Typesafe, customizable, clean & easy to use Redis client.|
|5|2|0|    * [bgc](https://github.com/viant/bgc) - Datastore Connectivity for BigQuery for go.|
|4|2|0|    * [dsc](https://github.com/viant/dsc) - Datastore connectivity for SQL, NoSQL, structured files.|
|2|1|0|    * [asc](https://github.com/viant/asc) - Datastore Connectivity for Aerospike for go.|
|0|0|0|    * [gomemcache](https://github.com/bradfitz/gomemcache/) - memcache client library for the Go programming language.|

*Libraries for working with dates and times.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|951|53|5|* [now](https://github.com/jinzhu/now) - Now is a time toolkit for golang.|
|164|11|0|* [durafmt](https://github.com/hako/durafmt) - Uime duration formatting library for Go.|
|139|4|0|* [timeutil](https://github.com/leekchan/timeutil) - Useful extensions (Timedelta, Strftime, ...) to the golang's time package.|
|125|12|5|* [carbon](https://github.com/uniplaces/carbon) - Simple Time extension with a lot of util methods, ported from PHP Carbon library.|
|38|7|2|* [dateparse](https://github.com/araddon/dateparse) - Parse date's without knowing format in advance.|
|26|2|0|* [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - The implementation of the Persian (Solar Hijri) Calendar in Go (golang).|
|12|3|0|* [goweek](https://github.com/grsmv/goweek) - Library for working with week entity in golang.|
|5|1|0|* [feiertage](https://github.com/wlbr/feiertage) - Set of functions to calculate public holidays in Germany, incl. specialization on the states of Germany (Bundesländer). Things like Easter, Pentecoast, Thanksgiving...|
|3|1|0|* [NullTime](https://github.com/kirillDanshin/nulltime) - Nullable `time.Time`.|
|1|0|1|* [tuesday](https://github.com/osteele/tuesday) - Ruby-compatible Strftime function.|

*Packages that help with building Distributed Systems.*

    * [dht](https://godoc.org/github.com/anacrolix/dht) - BitTorrent Kademlia DHT implementation.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|7596|753|33|* [go-kit](https://github.com/go-kit/kit) - Microservice toolkit with support for service discovery, load balancing, pluggable transports, request tracking, etc.|
|3832|713|98|* [grpc-go](https://github.com/grpc/grpc-go) - The Go language implementation of gRPC. HTTP/2 based RPC.|
|3501|256|1|* [micro](https://github.com/micro/micro) - Pluggable microservice toolkit and distributed systems platform.|
|3335|360|47|* [NATS](https://github.com/nats-io/gnatsd) - Lightweight, high performance messaging system for microservices, IoT, and cloud native systems.|
|1784|180|19|* [torrent](https://github.com/anacrolix/torrent) - BitTorrent client package.|
|1717|147|9|* [glow](https://github.com/chrislusf/glow) - Easy-to-Use scalable distributed big data processing, Map-Reduce, DAG execution, all in pure Go.|
|1386|245|11|* [rpcx](https://github.com/smallnest/rpcx) - Distributed pluggable RPC service framework like alibaba Dubbo.|
|1313|167|56|* [raft](https://github.com/hashicorp/raft) - Golang implementation of the Raft consensus protocol, by HashiCorp.|
|849|87|5|* [gleam](https://github.com/chrislusf/gleam) - Fast and scalable distributed map/reduce system written in pure Go and Luajit, combining Go's high concurrency with Luajit's high performance, runs standalone or distributed.|
|624|128|108|* [tendermint](https://github.com/tendermint/tendermint) - High-performance middleware for transforming a state machine written in any programming language into a Byzantine Fault Tolerant replicated state machine using the Tendermint consensus and blockchain protocols.|
|615|123|6|* [hprose](https://github.com/hprose/hprose-golang) - Very newbility RPC Library, support 25+ languages now.|
|390|51|11|* [gorpc](https://github.com/valyala/gorpc) - Simple, fast and scalable RPC library for high load.|
|361|30|23|* [ringpop-go](https://github.com/uber/ringpop-go) - Scalable, fault-tolerant application-layer sharding for Go applications.|
|281|41|7|    * [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) - Video streaming torrent client.|
|232|13|0|* [sleuth](https://github.com/ursiform/sleuth) - Library for master-less p2p auto-discovery and RPC between HTTP services (using [ZeroMQ](https://github.com/zeromq/libzmq)).|
|131|8|9|* [digota](https://github.com/digota/digota) - grpc ecommerce microservice.|
|127|11|0|* [go-jump](https://github.com/dgryski/go-jump) - Port of Google's "Jump" Consistent Hash function.|
|95|16|2|* [KrakenD](https://github.com/devopsfaith/krakend) - Ultra performant API Gateway framework with middlewares.|
|32|2|0|* [jsonrpc](https://github.com/osamingo/jsonrpc) - The jsonrpc package helps implement of JSON-RPC 2.0.|
|31|1|0|* [flowgraph](https://github.com/vectaport/flowgraph) - MPI-style ready-send coordination layer.|
|26|3|0|* [celeriac](https://github.com/svcavallar/celeriac.v1) - Library for adding support for interacting and monitoring Celery workers, tasks and events in Go.|
|18|10|0|* [drmaa](https://github.com/dgruber/drmaa) - Job submission library for cluster schedulers based on the DRMAA standard.|
|9|2|0|* [jsonrpc](https://github.com/ybbus/jsonrpc) - JSON-RPC 2.0 HTTP client implementation.|
|0|0|0|* [raft](https://github.com/coreos/etcd/tree/master/raft) - Go implementation of the Raft consensus protocol, by CoreOS.|

*Libraries that implement email creation and sending.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2413|150|55|* [MailHog](https://github.com/mailhog/MailHog) - Email and SMTP testing with web and API interface.|
|969|33|4|* [hermes](https://github.com/matcornic/hermes) - Golang package that generates clean, responsive HTML e-mails.|
|791|90|24|* [email](https://github.com/jordan-wright/email) - A robust and flexible email library for Go.|
|269|29|17|* [go-imap](https://github.com/emersion/go-imap) - IMAP library for clients and servers.|
|269|72|13|* [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid's Go library for sending email.|
|120|10|9|* [Hectane](https://github.com/hectane/hectane) - Lightweight SMTP client providing an HTTP API.|
|97|18|11|* [douceur](https://github.com/aymerick/douceur) - CSS inliner for your HTML emails.|
|34|4|0|* [smtp](https://github.com/mailhog/smtp) - SMTP server protocol state machine.|
|30|10|1|* [go-dkim](https://github.com/toorop/go-dkim) - DKIM library, to sign & verify email.|
|25|6|3|* [go-message](https://github.com/emersion/go-message) - Streaming library for the Internet Message Format and mail messages.|
|0|0|0|* [Gomail](https://github.com/go-gomail/gomail/) - Gomail is a very simple and powerful package to send emails.|

*Embedding other languages inside your go code.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3147|268|65|* [otto](https://github.com/robertkrimen/otto) - JavaScript interpreter written in Go.|
|1771|158|12|* [gopher-lua](https://github.com/yuin/gopher-lua) - Lua 5.1 VM and compiler written in Go.|
|1043|62|26|* [go-lua](https://github.com/Shopify/go-lua) - Port of the Lua 5.2 VM to pure Go.|
|528|53|14|* [go-python](https://github.com/sbinet/go-python) - naive go bindings to the CPython C-API.|
|518|53|2|* [go-duktape](https://github.com/olebedev/go-duktape) - Duktape JavaScript engine bindings for Go.|
|438|39|6|* [anko](https://github.com/mattn/anko) - Scriptable interpreter written in Go.|
|366|26|2|* [gisp](https://github.com/jcla1/gisp) - Simple LISP in Go.|
|350|95|8|* [golua](https://github.com/aarzilli/golua) - Go bindings for Lua C API.|
|341|46|5|* [go-php](https://github.com/deuill/go-php) - PHP bindings for Go.|
|271|29|20|* [agora](https://github.com/PuerkitoBio/agora) - Dynamically typed, embeddable programming language in Go.|
|17|1|1|* [purl](https://github.com/ian-kent/purl) - Perl 5.18.2 embedded in Go.|
|8|0|0|* [ngaro](https://github.com/db47h/ngaro) - Embeddable Ngaro VM implementation enabling scripting in Retro.|
|4|0|0|* [binder](https://github.com/alexeyco/binder) - Go to Lua binding library, based on [gopher-lua](https://github.com/yuin/gopher-lua).|

*Libraries for  handling files and file systems.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1113|114|38|* [afero](https://github.com/spf13/afero) - FileSystem Abstraction System for Go.|
|263|36|23|* [notify](https://github.com/rjeczalik/notify) - File system event notification library with simple API, similar to os/signal.|
|11|0|0|* [tarfs](https://github.com/posener/tarfs) - Implementation of the [`FileSystem` interface](https://godoc.org/github.com/kr/fs#FileSystem) for tar files.|
|10|1|0|* [skywalker](https://github.com/dixonwille/skywalker) - Package to allow one to concurrently go through a filesystem with ease.|
|8|2|0|* [go-csv-tag](https://github.com/artonge/go-csv-tag) - Load csv file using tag.|
|3|0|0|* [go-gtfs](https://github.com/artonge/go-gtfs) - Load gtfs files in go.|

*Packages for accounting and finance.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|590|101|11|* [decimal](https://github.com/shopspring/decimal) - Arbitrary-precision fixed-point decimal numbers.|
|455|32|0|* [go-finance](https://github.com/FlashBoys/go-finance) - Comprehensive financial markets data in Go.|
|342|14|2|* [go-money](https://github.com/rhymond/go-money) - Implementation of Fowler's Money pattern.|
|306|13|1|* [accounting](https://github.com/leekchan/accounting) - money and currency formatting for golang.|
|35|1|3|* [vat](https://github.com/dannyvankooten/vat) - VAT number validation & EU VAT rates.|
|11|0|0|* [ofxgo](https://github.com/aclindsa/ofxgo) - Query OFX servers and/or parse the responses (with example command-line client).|

*Libraries for working with forms.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|767|53|7|* [nosurf](https://github.com/justinas/nosurf) - CSRF protection middleware for Go.|
|609|46|5|* [binding](https://github.com/mholt/binding) - Binds form and JSON data from net/http Request to struct.|
|229|37|4|* [gorilla/csrf](https://github.com/gorilla/csrf) - CSRF protection for Go web applications & services.|
|193|8|1|* [form](https://github.com/go-playground/form) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support.|
|87|8|1|* [conform](https://github.com/leebenson/conform) - Keeps user input in check. Trims, sanitizes & scrubs data based on struct tags.|
|78|6|2|* [formam](https://github.com/monoculum/formam) - decode form's values into a struct.|
|71|5|2|* [forms](https://github.com/albrow/forms) - Framework-agnostic library for parsing and validating form/JSON data which supports multipart forms and files.|
|13|2|0|* [bind](https://github.com/robfig/bind) - Bind form data to any Go values.|

*Awesome game development libraries.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1509|453|5|* [Leaf](https://github.com/name5566/leaf) - Lightweight game server framework.|
|850|272|0|* [gonet](https://github.com/xtaci/gonet) - Game server skeleton implemented with golang.|
|785|47|6|* [termloop](https://github.com/JoelOtter/termloop) - Terminal-based game engine for Go, built on top of Termbox.|
|684|35|8|* [Pixel](https://github.com/faiface/pixel) - Hand-crafted 2D game library in Go.|
|652|95|5|* [go-sdl2](https://github.com/veandco/go-sdl2) - Go bindings for the [Simple DirectMedia Layer](https://www.libsdl.org/).|
|643|65|68|* [engo](https://github.com/EngoEngine/engo) - Engo is an open-source 2D game engine written in Go. It follows the Entity-Component-System paradigm.|
|428|38|69|* [Ebiten](https://github.com/hajimehoshi/ebiten) - simple 2D game library in Go.|
|355|11|13|* [Oak](https://github.com/oakmound/oak) - Pure Go game engine.|
|295|17|78|* [Azul3D](https://github.com/azul3d/engine) - 3D game engine written in Go.|
|279|21|4|* [GarageEngine](https://github.com/vova616/GarageEngine) - 2d game engine written in Go working on OpenGL.|
|275|30|11|* [goworld](https://github.com/xiaonanln/goworld) - Scalable game server engine, featuring space-entity framework and hot-swapping|
|205|20|1|* [go-astar](https://github.com/beefsack/go-astar) - Go implementation of the A\* path finding algorithm.|
|161|8|0|* [raylib-go](https://github.com/gen2brain/raylib-go) - Go bindings for [raylib](http://www.raylib.com/), a simple and easy-to-use library to learn videogames programming.|
|126|14|0|* [go3d](https://github.com/ungerik/go3d) - Performance oriented 2D/3D math package for Go.|
|78|7|3|* [glop](https://github.com/runningwild/glop) - Glop (Game Library Of Power) is a fairly simple cross-platform game library.|
|11|0|0|* [go-collada](https://github.com/GlenKelley/go-collada) - Go package for working with the Collada file format.|
|0|0|0|* [nano](https://github.com/lonnng/nano) - Lightweight, facility, high performance golang based game server framework|

*Tools to enhance the language with features like generics via code generation.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1261|76|1|* [go-linq](https://github.com/ahmetalpbalkan/go-linq) - .NET LINQ-like query methods for Go.|
|825|60|29|* [gen](https://github.com/clipperhouse/gen) - Code generation tool for ‘generics’-like functionality.|
|507|19|0|* [jennifer](https://github.com/dave/jennifer) - Generate arbitrary Go code without templates.|
|111|4|0|* [interfaces](https://github.com/rjeczalik/interfaces) - Command line tool for generating interface definitions.|
|56|9|0|* [pkgreflect](https://github.com/ungerik/pkgreflect) - Go preprocessor for package scoped reflection.|
|21|4|2|* [efaceconv](https://github.com/t0pep0/efaceconv) - Code generation tool for high performance conversion from interface{} to immutable type without allocations.|
|16|1|0|* [go-enum](https://github.com/abice/go-enum) - Code generation for enums from code comments.|

*Tools for compiling Go to other languages.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5528|245|123|* [gopherjs](https://github.com/gopherjs/gopherjs) - Compiler from Go to JavaScript.|
|840|65|23|* [llgo](https://github.com/go-llvm/llgo) - LLVM-based compiler for Go.|
|347|18|3|* [tardisgo](https://github.com/tardisgo/tardisgo) - Golang to Haxe to CPP/CSharp/Java/JavaScript transpiler.|

*Tools for managing and working with Goroutines.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1775|138|20|* [goworker](https://github.com/benmanns/goworker) - goworker is a Go-based background worker.|
|571|46|6|* [tunny](https://github.com/Jeffail/tunny) - Goroutine pool for golang.|
|304|17|0|* [pool](https://github.com/go-playground/pool) - Limited consumer goroutine or unlimited goroutine pool for easier goroutine handling and cancellation.|
|232|26|1|* [grpool](https://github.com/ivpusic/grpool) - Lightweight Goroutine pool.|
|73|1|0|* [go-floc](https://github.com/workanator/go-floc) - Orchestrate goroutines with ease.|
|51|6|0|* [go-flow](https://github.com/kamildrazkiewicz/go-flow) - Control goroutines execution order.|
|6|2|2|* [semaphore](https://github.com/kamilsk/semaphore) - Semaphore pattern implementation with timeout of lock/unlock operations based on channel and context.|

*Libraries for building GUI Applications.*

*Toolkits*

* [go-gtk](http://mattn.github.io/go-gtk/) - Go bindings for GTK.

*Interaction*



|stars|forks|issues|description|
| --- | --- | --- | --- |
|4393|310|115|* [ui](https://github.com/andlabs/ui) - Platform-native GUI library for Go. Cross platform.|
|2864|172|118|* [qt](https://github.com/therecipe/qt) - Qt binding for Go (support for Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi).|
|2079|155|12|* [robotgo](https://github.com/go-vgo/robotgo) - Go Native cross-platform GUI system automation;Control the mouse, keyboard and other.|
|1999|352|110|* [walk](https://github.com/lxn/walk) - Windows application library kit for Go.|
|1814|178|62|* [go-qml](https://github.com/go-qml/qml) - QML support for the Go language.|
|1780|51|8|* [app](https://github.com/murlokswarm/app) - Package to create apps with GO, HTML and CSS. Supports: MacOS, Windows in progress.|
|1295|101|36|* [goqt](https://github.com/visualfc/goqt) - Golang bindings to the Qt cross-platform application framework.|
|692|84|20|* [go-sciter](https://github.com/sciter-sdk/go-sciter) - Go bindings for Sciter: the Embeddable HTML/CSS/script engine for modern desktop UI development. Cross platform.|
|493|26|2|* [go-astilectron](https://github.com/asticode/go-astilectron) - Build cross platform GUI apps with GO and HTML/JS/CSS (powered by Electron).|
|385|27|4|* [gosx-notifier](https://github.com/deckarep/gosx-notifier) - OSX Desktop Notifications library for Go.|
|278|58|8|* [gotk3](https://github.com/gotk3/gotk3) - Go bindings for GTK3.|
|221|38|13|* [systray](https://github.com/getlantern/systray) - Cross platform Go library to place an icon and menu in the notification area.|
|103|9|5|* [trayhost](https://github.com/shurcooL/trayhost) - Cross-platform Go library to place an icon in the host operating system's taskbar.|
|41|10|0|* [gowd](https://github.com/dtylman/gowd) - Rapid and simple desktop UI development with GO, HTML, CSS and NW.js. Cross platform.|

*Libraries, tools, and tutorials for interacting with hardware.*

See [go-hardware](https://github.com/rakyll/go-hardware) for a comprehensive list.

## Images

*Libraries for manipulating images.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1973|57|6|* [ln](https://github.com/fogleman/ln) - 3D line art rendering in Go.|
|1527|64|6|* [bild](https://github.com/anthonynsimon/bild) - Collection of image processing algorithms in pure Go.|
|1513|144|12|* [resize](https://github.com/nfnt/resize) - Image resizing for the Go with common interpolation methods.|
|1451|68|4|* [pt](https://github.com/fogleman/pt) - Path tracing engine written in Go.|
|1309|124|24|* [imaginary](https://github.com/h2non/imaginary) - Fast and simple HTTP microservice for image resizing.|
|1253|138|0|* [imaging](https://github.com/disintegration/imaging) - Simple Go image processing package.|
|1031|66|6|* [gg](https://github.com/fogleman/gg) - 2D rendering in pure Go.|
|934|60|0|* [gift](https://github.com/disintegration/gift) - Package of image processing filters.|
|914|39|2|* [geopattern](https://github.com/pravj/geopattern) - Create beautiful generative image patterns from a string.|
|911|49|3|* [smartcrop](https://github.com/muesli/smartcrop) - Finds good crops for arbitrary images and crop sizes.|
|754|132|32|* [go-opencv](https://github.com/lazywei/go-opencv) - Go bindings for OpenCV.|
|670|64|16|* [picfit](https://github.com/thoas/picfit) - An image resizing server written in Go.|
|610|83|7|* [imagick](https://github.com/gographics/imagick) - Go binding to ImageMagick's MagickWand C API.|
|346|71|34|* [bimg](https://github.com/h2non/bimg) - Small package for fast and efficient image processing using libvips.|
|229|27|1|* [go-nude](https://github.com/koyachi/go-nude) - Nudity detection with Go.|
|137|8|1|* [rez](https://github.com/bamiaux/rez) - Image resizing in pure Go and SIMD.|
|105|3|1|* [img](https://github.com/hawx/img) - Selection of image manipulation tools.|
|61|18|1|* [go-cairo](https://github.com/ungerik/go-cairo) - Go binding for the cairo graphics library.|
|40|11|0|* [go-gd](https://github.com/bolknote/go-gd) - Go binding for GD library.|
|21|0|0|* [go-webcolors](https://github.com/jyotiska/go-webcolors) - Port of webcolors library from Python to Go.|
|16|9|1|* [tga](https://github.com/ftrvxmtrx/tga) - Package tga is a TARGA image format decoder/encoder.|
|3|0|0|* [mpo](https://github.com/donatj/mpo) - Decoder and conversion tool for MPO 3D Photos.|
|0|0|0|* [svgo](https://github.com/ajstarks/svgo) - Go Language Library for SVG generation.|

*Libraries for programming devices of the IoT.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|539|143|41|* [gatt](https://github.com/paypal/gatt) - Gatt is a Go package for building Bluetooth Low Energy peripherals.|
|248|40|10|* [flogo](https://github.com/tibcosoftware/flogo) - Project Flogo is an Open Source Framework for IoT Edge Apps & Integration.|
|207|30|0|* [mainflux](https://github.com/Mainflux/mainflux) - Industrial IoT Messaging and Device Management Server.|
|189|14|9|* [devices](https://github.com/goiot/devices) - Suite of libraries for IoT devices, experimental for x/exp/io.|
|109|24|42|* [sensorbee](https://github.com/sensorbee/sensorbee) - Lightweight stream processing engine for IoT.|
|74|7|16|* [connectordb](https://github.com/connectordb/connectordb) - Open-Source Platform for Quantified Self & IoT.|
|7|2|9|* [eywa](https://github.com/xcodersun/eywa) - Project Eywa is essentially a connection manager that keeps track of connected devices.|
|0|0|0|* [gobot](https://github.com/hybridgroup/gobot/) - Gobot is a framework for robotics, physical computing, and the Internet of Things.|

*Libraries for generating and working with log files.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5423|770|86|* [logrus](https://github.com/Sirupsen/logrus) - Structured logger for Go.|
|2745|173|12|* [zap](https://github.com/uber-go/zap) - Fast, structured, leveled logging in Go.|
|1551|101|13|* [spew](https://github.com/davecgh/go-spew) - Implements a deep pretty printer for Go data structures to aid in debugging.|
|1484|307|2|* [glog](https://github.com/golang/glog) - Leveled execution logs for Go.|
|955|172|24|* [seelog](https://github.com/cihub/seelog) - Logging functionality with flexible dispatching, filtering, and formatting.|
|816|191|29|* [tail](https://github.com/hpcloud/tail) - Go package striving to emulate the features of the BSD tail program.|
|622|80|40|* [log15](https://github.com/inconshreveable/log15) - Simple, powerful logging for Go.|
|568|83|6|* [lumberjack](https://github.com/natefinch/lumberjack) - Simple rolling logger, implements io.WriteCloser.|
|434|18|5|* [zerolog](https://github.com/rs/zerolog) - Zero-allocation JSON logger.|
|429|38|7|* [log](https://github.com/apex/log) - Structured logging package for Go.|
|298|31|20|* [logxi](https://github.com/mgutz/logxi) - 12-factor app logger that is fast and makes you happy.|
|215|14|3|* [log](https://github.com/go-playground/log) - Simple, configurable and scalable Structured Logging for Go.|
|176|18|2|* [logutils](https://github.com/hashicorp/logutils) - Utilities for slightly better logging in Go (Golang) extending the standard logger.|
|163|21|2|* [go-logger](https://github.com/apsdehal/go-logger) - Simple logger of Go Programs, with level handlers.|
|105|9|0|* [xlog](https://github.com/rs/xlog) - Structured logger for `net/context` aware HTTP handlers with flexible dispatching.|
|74|9|0|* [logger](https://github.com/azer/logger) - Minimalistic logging library for Go.|
|74|17|4|* [ozzo-log](https://github.com/go-ozzo/ozzo-log) - High performance logging supporting log severity, categorization, and filtering. Can send filtered log messages to various targets (e.g. console, network, mail).|
|70|7|9|* [log-voyage](https://github.com/firstrow/logvoyage) - Full-featured logging saas written in golang.|
|42|4|1|* [stdlog](https://github.com/alexcesaro/log) - Stdlog is an object-oriented library providing leveled logging. It is very useful for cron jobs.|
|33|1|0|* [slf](https://github.com/ventu-io/slf) - The Structured Logging Facade (SLF) for Go (like SLF4J but structured and for Go).|
|28|6|0|* [logex](https://github.com/chzyer/logex) - Golang log lib, supports tracking and level, wrap by standard log lib.|
|26|5|0|* [gologger](https://github.com/sadlil/gologger) - Simple easy to use log lib for go, logs in Colored Console, Simple Console, File or Elasticsearch.|
|24|9|2|* [go-log](https://github.com/ian-kent/go-log) - Log4j implementation in Go.|
|22|1|1|* [slog](https://github.com/ventu-io/slog) - The reference implementation of the Structured Logging Facade (SLF) for Go.|
|17|8|0|* [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) plug-in to send errors to a [Loggly](https://www.loggly.com/).|
|14|5|1|* [go-log](https://github.com/siddontang/go-log) - Log lib supports level and multi handlers.|
|11|9|0|* [mlog](https://github.com/jbrodriguez/mlog) - Simple logging module for go, with 5 levels, an optional rotating logfile feature and stdout/stderr output.|
|6|1|5|* [gomol](https://github.com/aphistic/gomol) - Multiple-output, structured logging for Go with extensible logging outputs.|
|4|0|0|* [logdump](https://github.com/ewwwwwqm/logdump) - Package for multi-level logging.|
|2|1|0|* [glg](https://github.com/kpango/glg) - glg is simple and fast leveled logging library for Go.|
|1|0|0|* [go-cronowriter](https://github.com/utahta/go-cronowriter) - Simple writer that rotate log files automatically based on current date and time, like cronolog.|
|1|0|0|* [xlog](https://github.com/xfxdev/xlog) - Plugin architecture and flexible log system for Go, with level ctrl, multiple log target and custom log format.|
|0|0|0|* [gone/log](https://github.com/One-com/gone/tree/master/log) - Fast, extendable, full-featured, std-lib source compatible log library.|

*Libraries for Machine Learning.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|4450|521|45|* [GoLearn](https://github.com/sjwhitworth/golearn) - General Machine Learning library for Go.|
|1254|126|50|* [gorgonia](https://github.com/chewxy/gorgonia) - graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms.|
|749|57|5|* [goml](https://github.com/cdipaolo/goml) - On-line Machine Learning in Go.|
|545|68|30|* [CloudForest](https://github.com/ryanbressler/CloudForest) - Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go.|
|479|75|6|* [bayesian](https://github.com/jbrukh/bayesian) - Naive Bayesian Classification for Golang.|
|349|20|2|* [gago](https://github.com/MaxHalford/gago) - Multi-population, flexible, parallel genetic algorithm.|
|203|27|4|* [gobrain](https://github.com/goml/gobrain) - Neural Networks written in go.|
|164|13|0|* [regommend](https://github.com/muesli/regommend) - Recommendation & collaborative filtering engine.|
|150|37|0|* [go-galib](https://github.com/thoj/go-galib) - Genetic Algorithms library written in Go / golang.|
|105|23|5|* [shield](https://github.com/eaigner/shield) - Bayesian text classifier with flexible tokenizers and storage backends for Go.|
|90|20|2|* [go-fann](https://github.com/white-pony/go-fann) - Go bindings for Fast Artificial Neural Networks(FANN) library.|
|83|8|0|* [goRecommend](https://github.com/timkaye11/goRecommend) - Recommendation Algorithms library written in Go.|
|58|4|0|* [goga](https://github.com/tomcraven/goga) - Genetic algorithm library for Go.|
|55|9|1|* [neural-go](https://github.com/schuyler/neural-go) - Multilayer perceptron network implemented in Go, with training via backpropagation.|
|48|10|0|* [go-pr](https://github.com/daviddengcn/go-pr) - Pattern recognition package in Go lang.|
|34|10|0|* [golinear](https://github.com/danieldk/golinear) - liblinear bindings for Go.|
|27|2|3|* [neat](https://github.com/jinyeom/neat) - Plug-and-play, parallel Go framework for NeuroEvolution of Augmenting Topologies (NEAT).|
|3|0|0|* [mlgo](https://github.com/NullHypothesis/mlgo) - This project aims to provide minimalistic machine learning algorithms in Go.|
|0|0|0|* [probab](https://github.com/ThePaw/probab) - Probability distribution functions. Bayesian inference. Written in pure Go.|
|0|0|0|* [libsvm](https://github.com/datastream/libsvm) - libsvm golang version derived work based on LIBSVM 3.14.|
|0|0|0|* [godist](https://github.com/e-dard/godist) - Various probability distributions, and associated methods.|

*Libraries that implement messaging systems.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2092|404|26|* [sarama](https://github.com/Shopify/sarama) - Go library for Apache Kafka.|
|2054|161|6|* [Centrifugo](https://github.com/centrifugal/centrifugo) - Real-time messaging (Websockets or SockJS) server in Go.|
|1809|279|65|* [go-socket.io](https://github.com/googollee/go-socket.io) - socket.io library for golang, a realtime application framework.|
|1682|173|16|* [machinery](https://github.com/RichardKnop/machinery) - Asynchronous task queue/job queue based on distributed message passing.|
|1555|493|4|* [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster is a go push server cluster.|
|1300|183|7|* [NATS Go Client](https://github.com/nats-io/nats) - Lightweight and high performance publish-subscribe and distributed queueing messaging system - this is the Go library.|
|1237|137|16|* [gorush](https://github.com/appleboy/gorush) - Push notification server using [APNs2](https://github.com/sideshow/apns2) and google [GCM](https://github.com/google/go-gcm).|
|1192|103|22|* [mangos](https://github.com/go-mangos/mangos) - Pure go implementation of the Nanomsg ("Scalable Protocols") with transport interoperability.|
|917|154|47|* [Uniqush-Push](https://github.com/uniqush/uniqush-push) - Redis backed unified push service for server-side notifications to mobile devices.|
|857|197|10|* [go-nsq](https://github.com/nsqio/go-nsq) - the official Go package for NSQ.|
|680|74|3|* [melody](https://github.com/olahol/melody) - Minimalist framework for dealing with websocket sessions, includes broadcasting and automatic ping/pong handling.|
|560|85|13|* [zmq4](https://github.com/pebbe/zmq4) - Go interface to ZeroMQ version 4. Also available for [version 3](https://github.com/pebbe/zmq3) and [version 2](https://github.com/pebbe/zmq2).|
|556|51|21|* [Gollum](https://github.com/trivago/gollum) - A n:m multiplexer that gathers messages from different sources and broadcasts them to a set of destinations.|
|342|23|2|* [golongpoll](https://github.com/jcuga/golongpoll) - HTTP longpoll server library that makes web pub-sub simple.|
|284|32|4|* [EventBus](https://github.com/asaskevich/EventBus) - The lightweight event bus with async compatibility.|
|231|13|4|* [Glue](https://github.com/desertbit/glue) - Robust Go and Javascript Socket Library (Alternative to Socket.io).|
|166|53|23|* [dbus](https://github.com/godbus/dbus) - Native Go bindings for D-Bus.|
|141|22|1|* [pubsub](https://github.com/tuxychandru/pubsub) - Simple pubsub package for go.|
|140|9|0|* [emitter](https://github.com/olebedev/emitter) - Emits events using Go way, with wildcard, predicates, cancellation possibilities and many other good wins.|
|103|11|5|* [guble](https://github.com/smancke/guble) - Messaging server using push notifications (Google Firebase Cloud Messaging, Apple Push Notification services, SMS) as well as websockets, a REST API, featuring distributed operation and message-persistence.|
|82|10|2|* [oplog](https://github.com/dailymotion/oplog) - Generic oplog/replication system for REST APIs.|
|37|3|2|* [drone-line](https://github.com/appleboy/drone-line) - Sending [Line](https://business.line.me/en/services/bot) notifications using a binary, docker or Drone CI.|
|30|5|0|* [goose](https://github.com/ian-kent/goose) - Server Sent Events in Go.|
|29|7|0|* [go-notify](https://github.com/TheCreeper/go-notify) - Native implementation of the freedesktop notification spec.|
|27|3|0|* [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ is a lightweight and reliable library for managing of the local messages queue.|
|21|5|0|* [go-longpoll](https://github.com/ventu-io/go-longpoll) - PubSub with long polling.|
|2|0|0|* [event](https://github.com/agoalofalife/event) - Implementation of the pattern observer.|
|2|0|2|* [go-vitotrol](https://github.com/maxatome/go-vitotrol) - Client library to Viessmann Vitotrol web service.|
|0|0|0|* [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) - A tiny wrapper around NSQ topic and channel.|
|0|0|0|* [gaurun-client](https://github.com/osamingo/gaurun-client) - Gaurun Client written in Go.|

*These libraries were placed here because none of the other categories seemed to fit.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2190|114|27|* [errors](https://github.com/pkg/errors) - Package that provides simple error handling primitives.|
|1886|425|49|* [gopsutil](https://github.com/shirou/gopsutil) - Cross-platform library for retrieving process and system utilization(CPU, Memory, Disks, etc).|
|1325|176|17|* [go.uuid](https://github.com/satori/go.uuid) - Implementation of Universally Unique Identifier (UUID). Supported both creation and parsing of UUIDs.|
|1038|88|3|* [gosms](https://github.com/haxpax/gosms) - Your own local SMS gateway in Go that can be used to send SMS.|
|648|56|10|* [archiver](https://github.com/mholt/archiver) - Library and command for making and extracting .zip and .tar.gz archives.|
|516|38|4|* [go-resiliency](https://github.com/eapache/go-resiliency) - Resiliency patterns for golang.|
|399|25|17|* [jobs](https://github.com/albrow/jobs) - Persistent and flexible background jobs library.|
|390|31|2|* [xstrings](https://github.com/huandu/xstrings) - Collection of useful string functions ported from other languages.|
|386|55|2|* [go-commons-pool](https://github.com/jolestar/go-commons-pool) - Generic object pool for Golang.|
|329|21|5|* [go-multierror](https://github.com/hashicorp/go-multierror) - Go (golang) package for representing a list of errors as a single error.|
|303|6|0|* [conv](https://github.com/cstockton/go-conv) - Package conv provides fast and intuitive conversions across Go types.|
|244|12|0|* [health](https://github.com/dimiro1/health) - Easy to use, extensible health check library.|
|237|56|5|* [go-chat-bot](https://github.com/go-chat-bot/bot) - IRC, Slack & Telegram bot written in Go.|
|166|6|1|* [go-shortid](https://github.com/ventu-io/go-shortid) - Distributed generation of super short, unique, non-sequential, URL friendly IDs.|
|140|7|0|* [banner](https://github.com/dimiro1/banner) - Add beautiful banners into your Go applications.|
|133|13|1|* [gountries](https://github.com/pariz/gountries) - Package that exposes country and subdivision data.|
|107|10|1|* [slacker](https://github.com/shomali11/slacker) - Easy to use framework to create Slack bots.|
|71|4|2|* [battery](https://github.com/distatus/battery) - Cross-platform, normalized battery information library.|
|46|9|0|* [margelet](https://github.com/zhulik/margelet) - Framework for building Telegram bots.|
|42|3|0|* [gofakeit](https://github.com/brianvoe/gofakeit) - Random data generator written in go.|
|32|5|0|* [hanu](https://github.com/sbstjn/hanu) - Framework for writing Slack bots.|
|30|2|0|* [bitio](https://github.com/icza/bitio) - Highly optimized bit-level Reader and Writer for Go.|
|25|3|1|* [xkg](https://github.com/go-xkg/xkg) - X Keyboard Grabber.|
|24|2|0|* [indigo](https://github.com/osamingo/indigo) - Distributed unique ID generator of using Sonyflake and encoded by Base58.|
|24|8|1|* [browscap_go](https://github.com/digitalcrab/browscap_go) - GoLang Library for [Browser Capabilities Project](http://browscap.org/).|
|18|1|0|* [autoflags](https://github.com/artyom/autoflags) - Go package to automatically define command line flags from struct fields.|
|17|1|1|* [datacounter](https://github.com/miolini/datacounter) - Go counters for readers/writer/http.ResponseWriter.|
|15|0|0|* [go-sarah](https://github.com/oklahomer/go-sarah) - Framework to build bot for desired chat services including LINE, Slack, Gitter and more.|
|14|2|0|* [go-unarr](https://github.com/gen2brain/go-unarr) - Decompression library for RAR, TAR, ZIP and 7z archives.|
|11|0|0|* [goid](https://github.com/jakehl/goid) - Generate and Parse RFC4122 compliant V4 UUIDs.|
|5|1|0|* [werr](https://github.com/txgruppi/werr) - Error Wrapper creates an wrapper for the error type in Go which captures the File, Line and Stack of where it was called.|
|5|1|0|* [alice](https://github.com/magic003/alice) - Additive dependency injection container for Golang.|
|5|0|0|* [secdl](https://github.com/xor-gate/secdl) - Lighttpd ModSecDownload algorithm ported to go to secure download urls.|
|3|0|0|* [avgRating](https://github.com/kirillDanshin/avgRating) - Calculate average score and rating based on Wilson Score Equation.|
|2|0|0|* [uuid](https://github.com/agext/uuid) - Generate, encode, and decode UUIDs v1 with fast or cryptographic-quality random node identifier.|
|0|0|0|* [stats](https://github.com/go-playground/stats) - Monitors Go MemStats + System stats such as Memory, Swap and CPU and sends via UDP anywhere you want for logging etc...|
|0|0|0|* [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - Generate boilerplate http input and ouput handling.|
|0|0|0|* [go-openapi](https://github.com/go-openapi) - Collection of packages to parse and utilize open-api schemas.|

*Libraries for working with human languages.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|727|21|1|* [when](https://github.com/olebedev/when) - Natural EN and RU language date/time parser with pluggable rules.|
|380|76|11|* [gojieba](https://github.com/yanyiwu/gojieba) - This is a Go implementation of [jieba](https://github.com/fxsjy/jieba) which a Chinese word splitting algorithm.|
|281|10|0|* [nlp](https://github.com/Shixzie/nlp) - Extract values from strings and fill your structs with nlp.|
|233|8|2|* [whatlanggo](https://github.com/abadojack/whatlanggo) - Natural language detection package for Go. Supports 84 languages and 24 scripts (writing systems e.g. Latin, Cyrillic, etc).|
|206|15|3|* [sentences](https://github.com/neurosnap/sentences) - Sentence tokenizer:  converts text into a list of sentences.|
|197|7|2|* [prose](https://github.com/jdkato/prose) - Library for text processing that supports tokenization, part-of-speech tagging, named-entity extraction, and more.|
|67|11|0|* [go-nlp](https://github.com/nuance/go-nlp) - Utilities for working with discrete probability distributions and other tools useful for doing NLP work.|
|54|19|2|* [gounidecode](https://github.com/fiam/gounidecode) - Unicode transliterator (also known as unidecode) for Go.|
|52|4|0|* [nlp](https://github.com/james-bowman/nlp) - Go Natural Language Processing library supporting LSA (Latent Semantic Analysis).|
|52|11|0|* [MMSEGO](https://github.com/awsong/MMSEGO) - This is a GO implementation of [MMSEG](http://technology.chtsai.org/mmseg/) which a Chinese word splitting algorithm.|
|49|9|0|* [textcat](https://github.com/pebbe/textcat) - Go package for n-gram based text categorization, with support for utf-8 and raw text.|
|42|11|0|* [go-stem](https://github.com/agonopol/go-stem) - Implementation of the porter stemming algorithm.|
|35|2|0|* [stemmer](https://github.com/dchest/stemmer) - Stemmer packages for Go programming language. Includes English and German stemmers.|
|29|3|0|* [porter2](https://github.com/zhenjl/porter2) - Really fast Porter 2 stemmer.|
|29|4|3|* [segment](https://github.com/blevesearch/segment) - Go library for performing Unicode Text Segmentation as described in [Unicode Standard Annex #29](http://www.unicode.org/reports/tr29/)|
|22|3|0|* [go2vec](https://github.com/danieldk/go2vec) - Reader and utility functions for word2vec embeddings.|
|18|2|1|* [RAKE.go](https://github.com/Obaied/RAKE.go) - Go port of the Rapid Automatic Keyword Extraction Algorithm (RAKE).|
|17|5|2|* [paicehusk](https://github.com/rookii/paicehusk) - Golang implementation of the Paice/Husk Stemming Algorithm.|
|16|2|1|* [go-unidecode](https://github.com/mozillazg/go-unidecode) - ASCII transliterations of Unicode text.|
|14|1|1|* [snowball](https://github.com/goodsign/snowball) - Snowball stemmer port (cgo wrapper) for Go. Provides word stem extraction functionality [Snowball native](http://snowball.tartarus.org/).|
|14|2|2|* [icu](https://github.com/goodsign/icu) - Cgo binding for icu4c C library detection and conversion functions. Guaranteed compatibility with version 50.1.|
|12|5|0|* [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Go bindings for the snowball libstemmer library including porter 2.|
|7|0|0|* [go-mystem](https://github.com/dveselov/mystem) - CGo bindings to Yandex.Mystem - russian morphology analyzer.|
|7|6|0|* [libtextcat](https://github.com/goodsign/libtextcat) - Cgo binding for libtextcat C library. Guaranteed compatibility with version 2.2.|
|5|0|0|* [porter](https://github.com/a2800276/porter) - This is a fairly straightforward port of Martin Porter's C implementation of the Porter stemming algorithm.|
|2|1|2|* [go-eco](https://github.com/ThePaw/go-eco) - Similarity, dissimilarity and distance matrices; diversity, equitability and inequality measures; species richness estimators; coenocline models.|
|2|0|0|* [shamoji](https://github.com/osamingo/shamoji) - The shamoji is word filtering package written in Go.|
|0|0|0|* [go-i18n](https://github.com/nicksnyder/go-i18n/) - Package and an accompanying tool to work with localized text.|
|0|0|0|* [dpar](https://github.com/danieldk/dpar/) - Transition-based statistical dependency parser.|

*Libraries for working with various layers of the network.*

* [mqttPaho](https://eclipse.org/paho/clients/golang/) - The Paho Go Client provides an MQTT client library for connection to MQTT brokers via TCP, TLS or WebSockets.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|6057|1217|48|* [kcptun](https://github.com/xtaci/kcptun) - Extremely simple & fast udp tunnel based on KCP protocol.|
|4867|437|122|* [fasthttp](https://github.com/valyala/fasthttp) - Package fasthttp is a fast HTTP implementation for Go, up to 10 times faster than net/http.|
|2304|418|29|* [dns](https://github.com/miekg/dns) - Go library for working with DNS.|
|1424|282|41|* [gopacket](https://github.com/google/gopacket) - Go library for packet processing with libpcap bindings.|
|1028|175|29|* [gobgp](https://github.com/osrg/gobgp) - BGP implemented in the Go Programming Language.|
|770|163|7|* [kcp-go](https://github.com/xtaci/kcp-go) - KCP - Fast and Reliable ARQ Protocol.|
|473|34|12|* [ssh](https://github.com/gliderlabs/ssh) - Higher-level API for building SSH servers (wraps crypto/ssh).|
|390|121|10|* [sftp](https://github.com/pkg/sftp) - Package sftp implements the SSH File Transfer Protocol as described in https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt.|
|365|36|24|* [go-getter](https://github.com/hashicorp/go-getter) - Go library for downloading files or directories from various sources using a URL.|
|345|73|28|* [mdns](https://github.com/hashicorp/mdns) - Simple mDNS (Multicast DNS) client/server library in Golang.|
|321|58|2|* [lhttp](https://github.com/fanux/lhttp) - Powerful websocket framework, build your IM server more easily.|
|288|68|3|* [water](https://github.com/songgao/water) - Simple TUN/TAP library.|
|286|118|6|* [gotcp](https://github.com/gansidui/gotcp) - Go package for quickly writing tcp applications.|
|251|111|11|* [ftp](https://github.com/jlaffaye/ftp) - Package ftp implements a FTP client as described in [RFC 959](http://tools.ietf.org/html/rfc959).|
|220|65|18|* [gosnmp](https://github.com/soniah/gosnmp) - Native Go library for performing SNMP actions.|
|206|22|2|* [grab](https://github.com/cavaliercoder/grab) - Go package for managing file downloads.|
|173|19|3|* [buffstreams](https://github.com/stabbycutyou/buffstreams) - Streaming protocolbuffer data over TCP made easy.|
|162|32|4|* [go-stun](https://github.com/ccding/go-stun) - Go implementation of the STUN client (RFC 3489 and RFC 5389).|
|141|56|1|* [tcp_server](https://github.com/firstrow/tcp_server) - Go library for building tcp servers faster.|
|128|42|8|* [winrm](https://github.com/masterzen/winrm) - Go WinRM client to remotely execute commands on Windows machines.|
|112|11|0|* [ethernet](https://github.com/mdlayher/ethernet) - Package ethernet implements marshaling and unmarshaling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags.|
|112|15|6|* [raw](https://github.com/mdlayher/raw) - Package raw enables reading and writing data at the device driver level for a network interface.|
|108|24|3|* [utp](https://github.com/anacrolix/utp) - Go uTP micro transport protocol implementation.|
|95|17|1|* [arp](https://github.com/mdlayher/arp) - Package arp implements the ARP protocol, as described in RFC 826.|
|91|10|10|* [sslb](https://github.com/eduardonunesp/sslb) - It's a Super Simples Load Balancer, just a little project to achieve some kind of performance.|
|83|20|35|* [canopus](https://github.com/zubairhamed/canopus) - CoAP Client/Server implementation (RFC 7252).|
|64|6|0|* [jazigo](https://github.com/udhos/jazigo) - Jazigo is a tool written in Go for retrieving configuration for multiple network devices.|
|43|1|0|* [ether](https://github.com/songgao/ether) - Cross-platform Go package for sending and receiving ethernet frames.|
|31|4|0|* [portproxy](https://github.com/aybabtme/portproxy) - Simple TCP proxy which adds CORS support to API's which don't support it.|
|28|5|0|* [linkio](https://github.com/ian-kent/linkio) - Network link speed simulation for Reader/Writer interfaces.|
|27|9|2|* [dhcp6](https://github.com/mdlayher/dhcp6) - Package dhcp6 implements a DHCPv6 server, as described in RFC 3315.|
|19|3|1|* [xtcp](https://github.com/xfxdev/xtcp) - TCP Server Framework with simultaneous full duplex communication,graceful shutdown,custom protocol.|
|17|2|0|* [graval](https://github.com/koofr/graval) - Experimental FTP server framework.|
|10|1|0|* [publicip](https://github.com/polera/publicip) - Package publicip returns your public facing IPv4 address (internet egress).|
|7|1|0|* [golibwireshark](https://github.com/sunwxg/golibwireshark) - Package golibwireshark use libwireshark library to decode pcap file and analyse dissection data.|
|5|0|0|* [llb](https://github.com/kirillDanshin/llb) - It's a very simple but quick backend for proxy servers. Can be useful for fast redirection to predefined domain with zero memory allocation and fast response.|
|5|3|0|* [goshark](https://github.com/sunwxg/goshark) - Package goshark use tshark to decode IP packet and create data struct to analyse packet.|
|0|0|0|* [gopcap](https://github.com/akrennmair/gopcap) - Go wrapper for libpcap.|

*Libraries for using OpenGL in Go.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|403|49|7|* [glfw](https://github.com/go-gl/glfw) - Go bindings for GLFW 3.|
|384|35|10|* [gl](https://github.com/go-gl/gl) - Go bindings for OpenGL (generated via glow).|
|184|26|11|* [mathgl](https://github.com/go-gl/mathgl) - Pure Go math package specialized for 3D math, with inspiration from GLM.|
|96|8|4|* [goxjs/gl](https://github.com/goxjs/gl) - Go cross-platform OpenGL bindings (OS X, Linux, Windows, browsers, iOS, Android).|
|42|7|4|* [goxjs/glfw](https://github.com/goxjs/glfw) - Go cross-platform glfw library for creating an OpenGL context and receiving events.|

*Libraries that implement Object-Relational Mapping or datamapping techniques.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|6519|806|133|* [GORM](https://github.com/jinzhu/gorm) - The fantastic ORM library for Golang, aims to be developer friendly.|
|2552|306|104|* [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence, ORM-ish library for Go.|
|2261|340|100|* [Xorm](https://github.com/go-xorm/xorm) - Simple and powerful ORM for Go.|
|974|72|34|* [upper.io/db](https://github.com/upper/db) - Single interface for interacting with different data sources through the use of adapters that wrap mature database drivers.|
|749|64|40|* [SQLBoiler](https://github.com/volatiletech/sqlboiler) - ORM generator. Generate a featureful and blazing-fast ORM tailored to your database schema.|
|546|19|49|* [reform](https://github.com/go-reform/reform) - Better ORM for Go, based on non-empty interfaces and code generation.|
|460|87|9|* [QBS](https://github.com/coocood/qbs) - Stands for Query By Struct. A Go ORM.|
|271|43|32|* [pop/soda](https://github.com/markbates/pop) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.|
|168|10|3|* [Zoom](https://github.com/albrow/zoom) - Blazing-fast datastore and querying engine built on Redis.|
|83|8|0|* [go-store](https://github.com/gosuri/go-store) - Simple and fast Redis backed key-value store library for Go.|
|55|7|1|* [gomodel](https://github.com/cosiner/gomodel) - Lightweight, fast, orm-like library helps interactive with database.|
|0|0|0|* [beego orm](https://github.com/astaxie/beego/tree/master/orm) - Powerful orm framework for go. Support: pq/mysql/sqlite3.|
|0|0|0|* [go-pg](https://github.com/go-pg/pg) - PostgreSQL ORM with focus on PostgreSQL specific features and performance.|

*Libraries for package and dependency management.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5268|343|320|* [glide](https://github.com/Masterminds/glide) - Manage your golang vendor and vendored packages with ease. Inspired by tools like Maven, Bundler, and Pip.|
|4881|428|108|* [godep](https://github.com/tools/godep) - dependency tool for go, godep helps build packages reproducibly by fixing their dependencies.|
|4505|271|219|* [dep](https://github.com/golang/dep) - Go dependency tool.|
|2376|198|93|* [govendor](https://github.com/kardianos/govendor) - Go Package Manager. Go vendor tool that works with the standard vendor file.|
|1506|129|42|* [gopm](https://github.com/gpmgo/gopm) - Go Package Manager.|
|1276|91|16|* [gom](https://github.com/mattn/gom) - Go Manager - bundle for go.|
|1157|53|10|* [gpm](https://github.com/pote/gpm) - Barebones dependency manager for Go.|
|766|46|32|* [goop](https://github.com/nitrous-io/goop) - Simple dependency manager for Go (golang), inspired by Bundler.|
|682|61|39|* [gvt](https://github.com/FiloSottile/gvt) - `gvt` is a simple vendoring tool made for Go native vendoring (aka GO15VENDOREXPERIMENT), based on gb-vendor.|
|247|11|15|* [nut](https://github.com/jingweno/nut) - Vendor Go dependencies.|
|214|6|3|* [johnny-deps](https://github.com/VividCortex/johnny-deps) - Minimal dependency version using Git.|
|187|11|4|* [gigo](https://github.com/LyricalSecurity/gigo) - PIP-like dependency tool for golang, with support for private repositories and hashes.|
|104|5|3|* [VenGO](https://github.com/DamnWidget/VenGO) - create and manage exportable isolated go virtual environments.|
|30|6|0|* [gop](https://github.com/lunny/gop) - Build and manage your Go applications out of GOPATH|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1851|183|54|* [graphql-go](https://github.com/graphql-go/graphql) - Implementation of GraphQL for Go.|
|697|55|16|* [graphql](https://github.com/neelance/graphql-go) - GraphQL server with a focus on ease of use.|
|107|7|0|* [jsonql](https://github.com/elgs/jsonql) - JSON query expression library in Golang.|
|41|6|2|* [graphql](https://github.com/tmc/graphql) - graphql parser + utilities.|
|32|1|2|* [graphql](https://github.com/sevki/graphql) - GraphQL implementation in go.|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3102|242|65|* [go-bindata](https://github.com/jteeuwen/go-bindata) - Package that converts any file into managable Go source code.|
|1068|66|27|* [go.rice](https://github.com/GeertJohan/go.rice) - go.rice is a Go package that makes working with resources such as html,js,css,images and templates very easy.|
|649|40|5|* [statik](https://github.com/rakyll/statik) - Embeds static files into a Go executable.|
|226|39|5|* [esc](https://github.com/mjibson/esc) - Embeds files into Go programs and provides http.FileSystem interfaces to them.|
|178|12|4|* [vfsgen](https://github.com/shurcooL/vfsgen) - Generates a vfsdata.go file that statically implements the given virtual filesystem.|
|173|10|0|* [fileb0x](https://github.com/UnnoTed/fileb0x) - Simple tool to embed files in go with focus on "customization" and ease to use.|
|119|8|2|* [go-resources](https://github.com/omeid/go-resources) - Unfancy resources embedding with Go.|
|43|3|0|* [statics](https://github.com/go-playground/statics) - Embeds static resources into go files for single binary compilation + works with http.FileSystem + symlinks.|
|8|2|0|* [go-embed](https://github.com/pyros2097/go-embed) - Generates go code to embed resource files into your library or executable.|
|4|1|0|* [templify](https://github.com/wlbr/templify) - Embed external template files into Go code to create single file binaries.|

*Libraries for scientific computing and data analyzing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1295|113|49|* [streamtools](https://github.com/nytlabs/streamtools) - general purpose, graphical tool for dealing with streams of data.|
|757|58|9|* [stats](https://github.com/montanaflynn/stats) - Statistics package with common functions missing from the Golang standard library.|
|579|61|63|* [gonum/plot](https://github.com/gonum/plot) - gonum/plot provides an API for building and drawing plots in Go.|
|479|43|5|* [go-dsp](https://github.com/mjibson/go-dsp) - Digital Signal Processing for Go.|
|471|56|21|* [gonum/mat64](https://github.com/gonum/matrix) - The general purpose package for matrix computation. Package mat64 provides basic linear algebra operations for float64 matrices.|
|427|71|4|* [chart](https://github.com/vdobler/chart) - Simple Chart Plotting library for Go. Supports many graphs types.|
|398|48|1|* [goraph](https://github.com/gyuho/goraph) - Pure Go graph theory library(data structure, algorith visualization).|
|297|67|10|* [go.matrix](https://github.com/skelterjohn/go.matrix) - linear algebra for go (has been stalled).|
|186|16|0|* [ewma](https://github.com/VividCortex/ewma) - Exponentially-weighted moving averages.|
|111|17|1|* [blas](https://github.com/ziutek/blas) - Implementation of BLAS (Basic Linear Algebra Subprograms).|
|94|17|5|* [gohistogram](https://github.com/VividCortex/gohistogram) - Approximate histograms for data streams.|
|57|9|2|* [vectormath](https://github.com/spate/vectormath) - Vectormath for Go, an adaptation of the scalar C functions from Sony's Vector Math library, as found in the Bullet-2.79 source code (currently inactive).|
|33|12|1|* [geom](https://github.com/skelterjohn/geom) - 2D geometry for golang.|
|30|8|7|* [evaler](https://github.com/soniah/evaler) - Simple floating point arithmetic expression evaluator.|
|30|7|1|* [pagerank](https://github.com/alixaxel/pagerank) - Weighted PageRank algorithm implemented in Go.|
|18|6|4|* [gostat](https://github.com/ematvey/gostat) - Statistics library for the go language.|
|13|0|0|* [graph](https://github.com/yourbasic/graph) - Library of basic graph algorithms.|
|10|2|0|* [sparse](https://github.com/james-bowman/sparse) - Go Sparse matrix formats for linear algebra supporting scientific and machine learning applications, compatible with gonum matrix libraries.|
|6|2|0|* [gofrac](https://github.com/anschelsc/gofrac) - (goinstallable) fractions library for go with support for basic arithmetic.|
|6|1|5|* [go-fn](https://github.com/ematvey/go-fn) - Mathematical functions written in Go language, that are not covered by math pkg.|
|5|0|0|* [PiHex](https://github.com/claygod/PiHex) - Implementation of the "Bailey-Borwein-Plouffe" algorithm for the hexadecimal number Pi.|
|3|0|0|* [gocomplex](https://github.com/varver/gocomplex) - Complex number library for the Go programming language.|
|3|0|3|* [go-gt](https://github.com/ThePaw/go-gt) - Graph theory algorithms written in "Go" language.|
|2|0|1|* [ode](https://github.com/ChristopherRabotin/ode) - Ordinary differential equation (ODE) solver which supports extended states and channel-based iteration stop conditions.|

*Libraries that are used to help make your application more secure.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2062|227|59|* [lego](https://github.com/xenolf/lego) - Pure Go ACME client library and CLI tool (for use with Let's Encrypt).|
|1305|65|58|* [acmetool](https://github.com/hlandau/acme) - ACME (Let's Encrypt) client tool with automatic renewal.|
|747|41|0|* [secure](https://github.com/unrolled/secure) - HTTP middleware for Go that facilitates some quick security wins.|
|611|12|1|* [memguard](https://github.com/awnumar/memguard) - A pure Go library for handling sensitive values in memory.|
|208|6|0|* [BadActor](https://github.com/jaredfolkins/badactor) - In-memory, application-driven jailer built in the spirit of fail2ban.|
|164|9|1|* [passlib](https://github.com/hlandau/passlib) - Futureproof password hashing library.|
|118|14|2|* [simple-scrypt](https://github.com/elithrar/simple-scrypt) - Scrypt package with a simple, obvious API and automatic cost calibration built-in.|
|51|15|2|* [go-yara](https://github.com/hillu/go-yara) - Go Bindings for [YARA](https://github.com/plusvic/yara), the "pattern matching swiss knife for malware researchers (and everyone else)".|
|0|0|0|* [ssh-vault](https://github.com/ssh-vault/ssh-vault) - encrypt/decrypt using ssh keys.|

*Libraries and tools for binary serialization.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2066|497|102|* [goprotobuf](https://github.com/golang/protobuf) - Go support, in the form of a library and protocol compiler plugin, for Google's protocol buffers.|
|1244|102|5|* [jsoniter](https://github.com/json-iterator/go) - High-performance 100% compatible drop-in replacement of "encoding/json".|
|1144|158|52|* [gogoprotobuf](https://github.com/gogo/protobuf) - Protocol Buffers for Go with Gadgets.|
|1060|145|33|* [mapstructure](https://github.com/mitchellh/mapstructure) - Go library for decoding generic map values into native Go structures.|
|813|117|6|* [go-codec](https://github.com/ugorji/go) - High Performance, feature-Rich, idiomatic encode, decode and rpc library for msgpack, cbor and json, with runtime-based OR code-generation support.|
|264|21|8|* [colfer](https://github.com/pascaldekloe/colfer) - Code generation for the Colfer binary format.|
|254|21|0|* [go-capnproto](https://github.com/glycerine/go-capnproto) - Cap'n Proto library and parser for go.|
|75|26|2|* [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) - GoLang library for working with PHP session format and PHP Serialize/Unserialize functions.|
|61|5|0|* [structomap](https://github.com/tuvistavie/structomap) - Library to easily and dynamically generate maps from static structures.|
|57|8|3|* [bambam](https://github.com/glycerine/bambam) - generator for Cap'n Proto schemas from go.|
|17|9|6|* [asn1](https://github.com/PromonLogicalis/asn1) - Asn.1 BER and DER encoding library for golang.|

* [consul](https://www.consul.io/) - Consul is a tool for service discovery, monitoring and configuration.
* [nsq](http://nsq.io/) - A realtime distributed messaging platform.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|14729|2852|196|* [etcd](https://github.com/coreos/etcd) - Highly-available key value store for shared configuration and service discovery.|
|13803|944|84|* [Caddy](https://github.com/mholt/caddy) - Caddy is an alternative, HTTP/2 web server that's easy to configure and use.|
|8163|636|157|* [minio](https://github.com/minio/minio) - Minio is a distributed object storage server.|
|2388|104|6|* [devd](https://github.com/cortesi/devd) - Local webserver for developers.|
|365|21|1|* [algernon](https://github.com/xyproto/algernon) - HTTP/2 web server with built-in support for Lua, Markdown, GCSS and Amber.|
|18|4|5|* [yakvs](https://github.com/sci4me/yakvs) - Small, networked, in-memory key-value store.|

*Libraries and tools for templating and lexing.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1023|102|36|* [pongo2](https://github.com/flosch/pongo2) - Django-like template-engine for Go.|
|851|127|35|* [mustache](https://github.com/hoisie/mustache) - Go implementation of the Mustache template language.|
|792|48|10|* [quicktemplate](https://github.com/valyala/quicktemplate) - Fast, powerful, yet easy to use template engine. Converts templates into Go code and then compiles it.|
|792|39|14|* [hero](https://github.com/shiyanhui/hero) - Hero is a handy, fast and powerful go template engine.|
|742|44|17|* [amber](https://github.com/eknkc/amber) - Amber is an elegant templating engine for Go Programming Language It is inspired from HAML and Jade.|
|709|116|20|* [gofpdf](https://github.com/jung-kurt/gofpdf) - PDF document generator with high level support for text, drawing and images.|
|615|32|30|* [ace](https://github.com/yosssi/ace) - Ace is an HTML template engine for Go, inspired by Slim and Jade. Ace is a refinement of Gold.|
|593|70|9|* [Razor](https://github.com/sipin/gorazor) - Razor view engine for Golang.|
|399|22|9|* [jet](https://github.com/CloudyKit/jet) - Jet template engine.|
|322|25|10|* [ego](https://github.com/benbjohnson/ego) - Lightweight templating language that lets you write templates in Go. Templates are translated into Go and compiled.|
|186|16|9|* [raymond](https://github.com/aymerick/raymond) - Complete handlebars implementation in Go.|
|143|24|2|* [fasttemplate](https://github.com/valyala/fasttemplate) - Simple and fast template engine. Substitutes template placeholders up to 10x faster than [text/template](http://golang.org/pkg/text/template/).|
|120|18|6|* [Soy](https://github.com/robfig/soy) - Closure templates (aka Soy templates) for Go, following the [official spec](https://developers.google.com/closure/templates/).|
|70|5|2|* [kasia.go](https://github.com/ziutek/kasia.go) - Templating system for HTML and other text documents - go implementation.|
|60|1|3|* [grender](https://github.com/dannyvankooten/grender) - small wrapper around html/template for file-based templates that support extending other template files.|
|51|2|2|* [velvet](https://github.com/gobuffalo/velvet) - Complete handlebars implementation in Go.|
|27|3|4|* [liquid](https://github.com/osteele/liquid) - Go implementation of Shopify Liquid templates.|
|19|1|1|* [damsel](https://github.com/dskinner/damsel) - Markup language featuring html outlining via css-selectors, extensible via pkg html/template and others.|

*Libraries for testing codebases and generating test data.*

* Testing Frameworks
    * [ginkgo](http://onsi.github.io/ginkgo/) - BDD Testing Framework for Go.
    * [gocheck](http://labix.org/gocheck) - More advanced testing framework alternative to gotest.
    * [gomega](http://onsi.github.io/gomega/) - Rspec like matcher/assertion library.

* Mock

* Fuzzing and delta-debugging/reducing/shrinking.

* Selenium and browser control tools.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|3659|392|103|    * [Testify](https://github.com/stretchr/testify) - Sacred extension to the standard go testing package.|
|1936|114|20|    * [go-fuzz](https://github.com/dvyukov/go-fuzz) - Randomized testing system.|
|1416|64|33|    * [chromedp](https://github.com/knq/chromedp) - Way to drive/test Chrome, Safari, Edge, Android Webviews, and other browsers supporting the Chrome Debugging Protocol.|
|775|103|35|    * [gomock](https://github.com/golang/mock) - Mocking framework for the Go programming language.|
|747|43|7|    * [httpexpect](https://github.com/gavv/httpexpect) - Concise, declarative, and easy to use end-to-end HTTP and REST API testing.|
|542|76|3|    * [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) - Mock SQL driver for testing database interactions.|
|403|29|9|    * [goblin](https://github.com/franela/goblin) - Mocha like testing framework fo Go.|
|342|30|3|    * [gofuzz](https://github.com/google/gofuzz) - Library for populating go objects with random values.|
|338|12|4|    * [gock](https://github.com/h2non/gock) - Versatile HTTP mocking made easy.|
|276|10|7|    * [baloo](https://github.com/h2non/baloo) - Expressive and versatile end-to-end HTTP API testing made easy.|
|235|28|8|    * [godog](https://github.com/DATA-DOG/godog) - Cucumber or Behat like BDD framework for Go.|
|201|12|9|    * [frisby](https://github.com/verdverm/frisby) - REST API testing framework.|
|167|6|50|    * [Tavor](https://github.com/zimmski/tavor) - Generic fuzzing and delta-debugging framework.|
|162|28|19|    * [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - Tool for generating self-contained mock objects.|
|160|4|0|    * [go-carpet](https://github.com/msoap/go-carpet) - Tool for viewing test coverage in terminal.|
|152|10|4|    * [go-vcr](https://github.com/dnaeon/go-vcr) - Record and replay your HTTP interactions for fast, deterministic and accurate tests.|
|115|7|2|    * [testfixtures](https://github.com/go-testfixtures/testfixtures) - A helper for Rails' like test fixtures to test database applications.|
|109|17|4|    * [GoSpec](https://github.com/orfjackal/gospec) - BDD-style testing framework for the Go programming language.|
|107|6|16|    * [go-mutesting](https://github.com/zimmski/go-mutesting) - Mutation testing for Go source code.|
|103|5|2|    * [gofight](https://github.com/appleboy/gofight) - API Handler Testing for Golang Router framework.|
|74|4|0|    * [minimock](https://github.com/gojuno/minimock) - Mock generator for Go interfaces.|
|51|5|1|    * [gospecify](https://github.com/stesla/gospecify) - This provides a BDD syntax for testing your Go code. It should be familiar to anybody who has used libraries such as rspec.|
|40|1|4|    * [restit](https://github.com/yookoala/restit) - Go micro framework to help writing RESTful API integration test.|
|36|4|5|    * [cdp](https://github.com/mafredri/cdp) - Type-safe bindings for the Chrome Debugging Protocol that can be used with browsers or other debug targets that implement it.|
|27|3|0|    * [govcr](https://github.com/seborama/govcr) - HTTP mock for Golang: record and replay HTTP interactions for offline testing.|
|24|2|1|    * [Hamcrest](https://github.com/rdrdr/hamcrest) - fluent framework for declarative Matcher objects that, when applied to input values, produce self-describing results.|
|21|1|0|    * [wstest](https://github.com/posener/wstest) - Websocket client for unit-testing a websocket http.Handler.|
|19|3|0|    * [dbcleaner](https://github.com/khaiql/dbcleaner) - Clean database for testing purpose, inspired by `database_cleaner` in Ruby.|
|18|4|0|    * [mockhttp](https://github.com/tv42/mockhttp) - Mock object for Go http.ResponseWriter.|
|14|4|0|    * [bro](https://github.com/marioidival/bro) - Watch files in directory and run tests for them.|
|9|2|0|    * [assert](https://github.com/go-playground/assert) - Basic Assertion Library used along side native go testing, with building blocks for custom assertions.|
|8|0|4|    * [cupaloy](https://github.com/bradleyjkemp/cupaloy) - Simple snapshot testing addon for your test framework.|
|4|1|0|    * [ggr](https://github.com/aandryashin/ggr) - Lightweight server that routes and proxies Selenium Wedriver requests to multiple Selenium hubs.|
|4|2|0|    * [dsunit](https://github.com/viant/dsunit) - Datastore testing for SQL, NoSQL, structured files.|
|3|0|1|    * [gosuite](https://github.com/pavlo/gosuite) - Brings lightweight test suites with setup/teardown facilities to `testing` by leveraging Go1.7's Subtests.|
|2|1|0|    * [badio](https://github.com/cavaliercoder/badio) - Extensions to Go's `testing/iotest` package.|
|2|0|0|    * [selenoid](https://github.com/aandryashin/selenoid) - alternative Selenium hub server that launches browsers within containers.|
|0|0|0|    * [GoConvey](https://github.com/smartystreets/goconvey/) - BDD-style framework with web UI and live reload.|
|0|0|0|    * [go-txdb](https://github.com/DATA-DOG/go-txdb) - Single transaction based database driver mainly for testing purposes.|

*Libraries for parsing and manipulating texts.*

* Specific Formats
    * [github_flavored_markdown](https://godoc.org/github.com/shurcooL/github_flavored_markdown) - GitHub Flavored Markdown renderer (using blackfriday) with fenced code block highlighting, clickable header anchor links.
* Utility

|stars|forks|issues|description|
| --- | --- | --- | --- |
|4529|414|7|    * [GoQuery](https://github.com/PuerkitoBio/goquery) - GoQuery brings a syntax and a set of features similar to jQuery to the Go language.|
|2589|330|88|    * [blackfriday](https://github.com/russross/blackfriday) - Markdown processor in Go.|
|1560|205|20|    * [toml](https://github.com/BurntSushi/toml) - TOML configuration format (encoder/decoder with reflection).|
|1099|94|14|    * [go-humanize](https://github.com/dustin/go-humanize) - Formatters for time, numbers, and memory size to human readable format.|
|715|45|2|    * [bluemonday](https://github.com/microcosm-cc/bluemonday) - HTML Sanitizer.|
|709|41|2|    * [inject](https://github.com/facebookgo/inject) - Package inject provides a reflect based injector.|
|702|30|11|    * [sh](https://github.com/mvdan/sh) - Shell parser and formatter.|
|301|74|15|    * [go-pkg-rss](https://github.com/jteeuwen/go-pkg-rss) - This package reads RSS and Atom feeds and provides a caching mechanism that adheres to the feed specs.|
|279|17|0|    * [xurls](https://github.com/mvdan/xurls) - Extract urls from text.|
|198|44|0|    * [mxj](https://github.com/clbanning/mxj) - Encode / decode XML as JSON or map[string]interface{}; extract values with dot-notation paths and wildcards. Replaces x2j and j2x packages.|
|159|11|1|    * [gotabulate](https://github.com/bndr/gotabulate) - Easily pretty-print your tabular data with Go.|
|134|11|2|    * [gotext](https://github.com/leonelquinteros/gotext) - GNU gettext utilities for Go.|
|129|18|0|    * [slug](https://github.com/gosimple/slug) - URL-friendly slugify with multiple languages support.|
|126|23|7|    * [gographviz](https://github.com/awalterschulze/gographviz) - Parses the Graphviz DOT language.|
|93|19|1|    * [go-runewidth](https://github.com/mattn/go-runewidth) - Functions to get fixed width of the character or string.|
|40|4|0|    * [genex](https://github.com/alixaxel/genex) - Count and expand Regular Expressions into all matching Strings.|
|39|2|0|    * [goq](https://github.com/andrewstuart/goq) - Declarative unmarshaling of HTML using struct tags with jQuery syntax (uses GoQuery).|
|33|4|0|    * [guesslanguage](https://github.com/endeveit/guesslanguage) - Functions to determine the natural language of a unicode text.|
|27|4|1|    * [goregen](https://github.com/zach-klippenstein/goregen) - Library for generating random strings from regular expressions.|
|27|2|1|    * [align](https://github.com/Guitarbum722/align) - A general purpose application that aligns text.|
|24|1|1|    * [gonameparts](https://github.com/polera/gonameparts) - Parses human names into individual name parts.|
|23|0|0|    * [radix](https://github.com/yourbasic/radix) - fast string sorting algorithm.|
|15|4|0|    * [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) - Editorconfig file parser and manipulator for Go.|
|14|2|0|    * [go-slugify](https://github.com/mozillazg/go-slugify) - Make pretty slug with multiple languages support.|
|14|1|0|    * [parth](https://github.com/codemodus/parth) - URL path segmentation parsing.|
|13|0|0|    * [Slugify](https://github.com/avelino/slugify) - Go slugify application that handles string.|
|5|1|1|    * [kace](https://github.com/codemodus/kace) - Common case conversions covering common initialisms.|
|4|2|1|    * [go-vcard](https://github.com/emersion/go-vcard) - Parse and format vCard.|
|3|0|1|    * [parseargs-go](https://github.com/nproc/parseargs-go) - string argument parser that understands quotes and backslashes.|
|3|2|0|    * [enca](https://github.com/endeveit/enca) - Minimal cgo bindings for [libenca](http://cihar.com/software/enca/).|
|2|0|0|    * [bbConvert](https://github.com/CalebQ42/bbConvert) - Converts bbCode to HTML that allows you to add support for custom bbCode tags.|
|0|0|0|    * [gommon/bytes](https://github.com/labstack/gommon/tree/master/bytes) - Format bytes to string.|
|0|0|0|    * [doi](https://github.com/hscells/doi) - Document object identifier (doi) parser in Go.|
|0|0|0|    * [allot](https://github.com/sbstjn/allot) - Placeholder and wildcard text parsing for CLI tools and bots.|
|0|0|0|    * [gofeed](https://github.com/mmcdole/gofeed) - Parse RSS and Atom feeds in Go.|
|0|0|0|    * [go-nmea](https://github.com/adrianmo/go-nmea) - NMEA parser library for the Go language.|

*Libraries for accessing third party APIs.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|3399|716|59|* [aws-sdk-go](https://github.com/aws/aws-sdk-go) - The official AWS SDK for the Go programming language.|
|2853|672|44|* [github](https://github.com/google/go-github) - Go library for accessing the GitHub REST API v3.|
|1211|234|44|* [slack](https://github.com/nlopes/slack) - Slack API in Go.|
|1099|301|54|* [google](https://github.com/google/google-api-go-client) - Auto-generated Google APIs for Go.|
|823|241|96|* [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) - Google Cloud APIs Go Client Library.|
|758|186|61|* [anaconda](https://github.com/ChimeraCoder/anaconda) - Go client library for the Twitter 1.1 API.|
|672|245|96|* [goamz](https://github.com/mitchellh/goamz) - Popular fork of [goamz](https://launchpad.net/goamz) which adds some missing API calls to certain packages.|
|646|110|15|* [telegram-bot-api](https://github.com/Syfaro/telegram-bot-api) - Simple and clean Telegram bot client.|
|590|155|5|* [stripe](https://github.com/stripe/stripe-go) - Go client for the Stripe API.|
|493|148|2|* [facebook](https://github.com/huandu/facebook) - Go Library that supports the Facebook Graph API.|
|367|97|38|* [discordgo](https://github.com/bwmarrin/discordgo) - Go bindings for the Discord Chat API.|
|357|112|18|* [minio-go](https://github.com/minio/minio-go) - Minio Go Library for Amazon S3 compatible cloud storage.|
|324|66|10|* [telebot](https://github.com/tucnak/telebot) - Telegram bot framework written in Go.|
|305|60|11|* [go-twitter](https://github.com/dghubble/go-twitter) - Go client library for the Twitter v1.1 APIs.|
|202|17|2|* [geo-golang](https://github.com/codingsince1985/geo-golang) - Go Library to access [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro), [MapQuest](http://open.mapquestapi.com/geocoding/), [Nominatim](http://open.mapquestapi.com/nominatim/), [OpenCage](http://geocoder.opencagedata.com/api.html), [HERE](https://developer.here.com/rest-apis/documentation/geocoder), [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx), [Mapbox](https://www.mapbox.com/developers/api/geocoding/), and [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) geocoding / reverse geocoding APIs.|
|171|39|1|* [paypal](https://github.com/logpacker/paypalsdk) - Wrapper for PayPal payment API.|
|170|79|3|* [go-jira](https://github.com/andygrunwald/go-jira) - Go client library for [Atlassian JIRA](https://www.atlassian.com/software/jira)|
|150|97|20|* [go-marathon](https://github.com/gambol99/go-marathon) - Go library for interacting with Mesosphere's Marathon PAAS.|
|117|8|1|* [tbot](https://github.com/yanzay/tbot) - Telegram bot server with API similar to net/http.|
|113|2|4|* [githubql](https://github.com/shurcooL/githubql) - Go library for accessing the GitHub GraphQL API v4.|
|105|21|0|* [hipchat](https://github.com/andybons/hipchat) - This project implements a golang client library for the Hipchat API.|
|103|35|3|* [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) - A golang package to communicate with HipChat over XMPP.|
|102|14|1|* [webhooks](https://github.com/go-playground/webhooks) - Webhook receiver for GitHub and Bitbucket.|
|98|15|5|* [gostorm](https://github.com/jsgilmore/gostorm) - GoStorm is a Go library that implements the communications protocol required to write Storm spouts and Bolts in Go that communicate with the Storm shells.|
|82|2|0|* [go-trending](https://github.com/andygrunwald/go-trending) - Go library for accessing [trending repositories](https://github.com/trending) and [developers](https://github.com/trending/developers) at Github.|
|78|14|1|* [Medium](https://github.com/Medium/medium-sdk-go) - Golang SDK for Medium's OAuth2 API.|
|53|13|9|* [clarifai](https://github.com/samuelcouch/clarifai) - Go client library for interfacing with the Clarifai API.|
|47|8|0|* [megos](https://github.com/andygrunwald/megos) - Client library for accessing an [Apache Mesos](http://mesos.apache.org/) cluster.|
|46|0|0|* [go-tgbot](https://github.com/olebedev/go-tgbot) - Pure Golang Telegram Bot API wrapper, generated from swagger file, session-based router and middleware.|
|34|4|0|* [cachet](https://github.com/andygrunwald/cachet) - Go client library for [Cachet (open source status page system)](https://cachethq.io/).|
|33|1|0|* [go-telegraph](https://github.com/toby3d/go-telegraph) - Telegraph publishing platform API client.|
|30|2|0|* [gcm](https://github.com/Aorioli/gcm) - Go library for Google Cloud Messaging.|
|30|5|0|* [pushover](https://github.com/gregdel/pushover) - Go wrapper for the Pushover API.|
|25|22|5|* [gads](https://github.com/emiddleton/gads) - Google Adwords Unofficial API.|
|24|9|2|* [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) - Go MusicBrainz WS2 client library.|
|21|3|1|* [go-xkcd](https://github.com/nishanths/go-xkcd) - Go client for the xkcd API.|
|21|13|0|* [gami](https://github.com/bit4bit/gami) - Go library for Asterisk Manager Interface.|
|21|1|0|* [ghost](https://github.com/neuegram/ghost) - Go Library for accessing the Snapchat API.|
|20|6|0|* [mixpanel](https://github.com/dukex/mixpanel) - Mixpanel is a library for tracking events and sending Mixpanel profile updates to Mixpanel from your go applications.|
|19|5|0|* [Trello](https://github.com/adlio/trello) - Go wrapper for the Trello API.|
|18|1|0|* [golyrics](https://github.com/mamal72/golyrics) - Golyrics is a Go library to fetch music lyrics data from the Wikia website.|
|18|3|0|* [translate](https://github.com/poorny/translate) - Go online translation package.|
|17|8|0|* [fcm](https://github.com/maddevsio/fcm) - Go library for Firebase Cloud Messaging.|
|17|3|1|* [amazon-product-advertising-api](https://github.com/ngs/go-amazon-product-advertising-api) - Go Client Library for [Amazon Product Advertising API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html).|
|13|3|1|* [shopify](https://github.com/rapito/go-shopify) - Go Library to make CRUD request to the Shopify API.|
|12|1|0|* [spotify](https://github.com/rapito/go-spotify) - Go Library to access Spotify WEB API.|
|11|1|3|* [govkbot](https://github.com/nikepan/govkbot) - Simple Go [VK](https://vk.com) bot library.|
|11|0|5|* [brewerydb](https://github.com/naegelejd/brewerydb) - Go library for accessing the BreweryDB API.|
|10|1|0|* [TheMovieDb](https://github.com/jbrodriguez/go-tmdb) - Simple golang package to communicate with [themoviedb.org](https://themoviedb.org).|
|9|0|0|* [go-myanimelist](https://github.com/nstratos/go-myanimelist) - Go client library for accessing the [MyAnimeList API](http://myanimelist.net/modules.php?go=api).|
|8|2|7|* [go-twitch](https://github.com/knspriggs/go-twitch) - Go client for interacting with the Twitch v3 API.|
|8|2|0|* [steam](https://github.com/sostronk/go-steam) - Go Library to interact with Steam game servers.|
|7|1|0|* [google-analytics](https://github.com/chonthu/go-google-analytics) - Simple wrapper for easy google analytics reporting.|
|6|4|0|* [tumblr](https://github.com/mattcunningham/gumblr) - Go wrapper for the Tumblr v2 API.|
|5|1|0|* [go-imgur](https://github.com/koffeinsource/go-imgur) - Go client library for [imgur](https://imgur.com)|
|4|0|0|* [patreon-go](https://github.com/mxpv/patreon-go) - Go library for Patreon API.|
|4|3|0|* [google-email-audit-api](https://github.com/ngs/go-google-email-audit-api) - Go client library for [Google G Suite Email Audit API](https://developers.google.com/admin-sdk/email-audit/).|
|4|0|0|* [rrdaclient](https://github.com/Omie/rrdaclient) - Go Library to access statdns.com API, which is in turn RRDA API. DNS Queries over HTTP.|
|4|2|0|* [micha](https://github.com/onrik/micha) - Go Library for Telegram bot api.|
|2|0|0|* [go-hacknews](https://github.com/PaulRosset/go-hacknews) - Tiny Go client for HackerNews API.|
|2|2|10|* [go-unsplash](https://github.com/hbagdi/go-unsplash) - Go client library for the [Unsplash.com](https://unsplash.com) API.|
|1|3|0|* [zooz](https://github.com/gojuno/go-zooz) - Go client for the Zooz API.|
|0|0|0|* [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) - The Playlyfe Rest API Go SDK.|
|0|0|0|* [circleci](https://github.com/jszwedko/go-circleci) - Go client library for interacting with CircleCI's API.|
|0|0|0|* [textbelt](https://github.com/dietsche/textbelt) - Go client for the textbelt.com txt messaging API.|
|0|0|0|* [smite](https://github.com/sergiotapia/smitego) - Go package to wraps access to the Smite game API.|

*General utilities and tools to make your life easier.*

* [clockwerk](http://github.com/onatm/clockwerk) - Go package to schedule periodic jobs using a simple, fluent syntax.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|11242|1041|186|* [hub](https://github.com/github/hub) - wrap git commands with additional functionality to interact with github from the terminal.|
|11153|1727|60|* [ngrok](https://github.com/inconshreveable/ngrok) - Introspected tunnels to localhost.|
|10020|393|43|* [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder written in Go.|
|6750|229|28|* [wuzz](https://github.com/asciimoo/wuzz) - Interactive cli tool for HTTP inspection.|
|6285|451|90|* [delve](https://github.com/derekparker/delve) - Go debugger.|
|5982|189|22|* [ctop](https://github.com/bcicen/ctop) - [Top-like](http://ctop.sh) interface (e.g. htop) for container metrics.|
|4064|127|12|* [peco](https://github.com/peco/peco) - Simplistic interactive filtering tool.|
|3362|312|1|* [godropbox](https://github.com/dropbox/godropbox) - Common libraries for writing Go services/applications from Dropbox.|
|3230|276|83|* [sqlx](https://github.com/jmoiron/sqlx) - provides a set of extensions on top of the excellent built-in database/sql package.|
|2185|101|6|* [go-torch](https://github.com/uber/go-torch) - Stochastic flame graph profiler for Go programs.|
|2055|71|2|* [usql](https://github.com/knq/usql) - usql is a universal command-line interface for SQL databases.|
|1871|388|59|* [xlsx](https://github.com/tealeg/xlsx) - Library to simplify reading the XML format used by recent version of Microsoft Excel in Go programs.|
|1691|65|25|* [goreleaser](https://github.com/goreleaser/goreleaser) - Deliver Go binaries as fast and easily as possible.|
|1670|98|4|* [goreporter](https://github.com/wgliang/goreporter) - Golang tool that does static analysis, unit testing, code review and generate code quality report.|
|1667|93|3|* [GJSON](https://github.com/tidwall/gjson) - Get a JSON value with one line of code.|
|1598|61|7|* [realize](https://github.com/tockins/realize) - Go build system with file watchers and live reload. Run, build and watch file changes with custom paths.|
|1457|45|8|* [panicparse](https://github.com/maruel/panicparse) - Groups similar goroutines and colorizes stack dump.|
|1426|87|26|* [gojson](https://github.com/ChimeraCoder/gojson) - Automatically generate Go (golang) struct definitions from example JSON.|
|1389|117|41|* [excelize](https://github.com/Luxurioust/excelize) - Golang library for reading and writing Microsoft Excel (XLSX) files.|
|1284|165|48|* [gorequest](https://github.com/parnurzeal/gorequest) - Simplified HTTP client with rich features for Go.|
|1263|24|10|* [mmake](https://github.com/tj/mmake) - Modern Make.|
|1194|45|5|* [coop](https://github.com/rakyll/coop) - Cheat sheet for some of the common concurrent flows in Go.|
|1028|63|7|* [minify](https://github.com/tdewolff/minify) - Fast minifiers for HTML, CSS, JS, XML, JSON and SVG file formats.|
|914|53|15|* [grequests](https://github.com/levigross/grequests) - Elegant and simple `net/http` wrapper that follows Python's requests library.|
|912|47|3|* [go-underscore](https://github.com/tobyhede/go-underscore) - Useful collection of helpfully functional Go collection utilities.|
|683|95|23|* [hystrix-go](https://github.com/afex/hystrix-go) - Implements Hystrix patterns of programmer-defined fallbacks aka circuit breaker.|
|644|42|3|* [profile](https://github.com/pkg/profile) - Simple profiling support package for Go.|
|633|38|23|* [Storm](https://github.com/asdine/storm) - Simple and powerful toolkit for BoltDB.|
|601|89|20|* [goreq](https://github.com/franela/goreq) - Minimal and simple request library for Go language.|
|562|62|2|* [resty](https://github.com/go-resty/resty) - Simple HTTP and REST client for Go inspired by Ruby rest-client.|
|557|83|30|* [mc](https://github.com/minio/mc) - Minio Client provides minimal tools to work with Amazon S3 compatible cloud storage and filesystems.|
|549|47|4|* [sling](https://github.com/dghubble/sling) - Go HTTP requests builder for API clients.|
|538|36|29|* [boilr](https://github.com/tmrts/boilr) - Blazingly fast CLI tool for creating projects from boilerplate templates.|
|490|40|9|* [circuitbreaker](https://github.com/rubyist/circuitbreaker) - Circuit Breakers in Go.|
|467|15|3|* [gron](https://github.com/roylee0704/gron) - Define time-based tasks using a simple Go API and Gron’s scheduler will run them accordingly.|
|456|28|0|* [httpcontrol](https://github.com/facebookgo/httpcontrol) - Package httpcontrol allows for HTTP transport level control around timeouts and retries.|
|450|15|8|* [gentleman](https://github.com/h2non/gentleman) - Full-featured plugin-driven HTTP client library.|
|437|20|5|* [htcat](https://github.com/htcat/htcat) - Parallel and Pipelined HTTP GET Utility.|
|413|11|1|* [immortal](https://github.com/immortal/immortal) - *nix cross-platform (OS agnostic) supervisor.|
|394|30|4|* [gopencils](https://github.com/bndr/gopencils) - Small and simple package to easily consume REST APIs.|
|389|22|0|* [JobRunner](https://github.com/bamzi/jobrunner) - Smart and featureful cron job scheduler with job queuing and live monitoring built in.|
|373|32|13|* [go-debug](https://github.com/tj/go-debug) - Conditional debug logging for Golang libraries & applications.|
|369|19|25|* [git-time-metric](https://github.com/git-time-metric/gtm) - Simple, seamless, lightweight time tracking for Git.|
|368|11|7|* [Task](https://github.com/go-task/task) - simple "Make" alternative.|
|359|30|2|* [spinner](https://github.com/briandowns/spinner) - Go package to easily provide a terminal spinner with options.|
|318|28|3|* [godaemon](https://github.com/VividCortex/godaemon) - Utility to write daemons.|
|313|61|16|* [mergo](https://github.com/imdario/mergo) - Helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.|
|261|10|18|* [go-funk](https://github.com/thoas/go-funk) - Modern Go utility library which provides helpers (map, find, contains, filter, chunk, reverse, ...).|
|222|43|0|* [gohper](https://github.com/cosiner/gohper) - Various tools/modules help for development.|
|219|12|0|* [go-rate](https://github.com/beefsack/go-rate) - Timed rate limiter for Go.|
|215|19|3|* [request](https://github.com/mozillazg/request) - Go HTTP Requests for Humans™.|
|193|19|0|* [go-dry](https://github.com/ungerik/go-dry) - DRY (don't repeat yourself) package for Go.|
|192|20|4|* [pester](https://github.com/sethgrid/pester) - Go HTTP client calls with retries, backoff, and concurrency.|
|166|20|5|* [filetype](https://github.com/h2non/filetype) - Small package to infer the file type checking the magic numbers signature.|
|163|26|5|* [scheduler](https://github.com/carlescere/scheduler) - Cronjobs scheduling made easy.|
|147|4|0|* [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) - go:generate tool for wrapping symbols exported by golang plugins (1.8 only).|
|146|9|0|* [go-cron](https://github.com/rk/go-cron) - Simple Cron library for go that can execute closures or functions at varying intervals, from once a second to once a year on a specific date and time. Primarily for web applications and long running daemons.|
|134|5|0|* [moldova](https://github.com/StabbyCutyou/moldova) - Utility for generating random data based on an input template.|
|128|7|0|* [rerun](https://github.com/ivpusic/rerun) - Recompiling and rerunning go apps when source changes.|
|118|16|1|* [Deepcopier](https://github.com/ulule/deepcopier) - Simple struct copying for Go.|
|96|18|1|* [go-trigger](https://github.com/sadlil/go-trigger) - Go-lang global event triggerer, Register Events with an id and trigger the event from anywhere from your project.|
|89|17|6|* [apm](https://github.com/topfreegames/apm) - Process manager for Golang applications with an HTTP API.|
|79|7|0|* [gojq](https://github.com/elgs/gojq) - JSON query in Golang.|
|71|1|1|* [jsongo](https://github.com/ricardolonga/jsongo) - Fluent API to make it easier to create Json objects.|
|64|3|2|* [UNIS](https://github.com/esemplastic/unis) - Common Architecture™ for String Utilities in Go.|
|64|9|0|* [Death](https://github.com/vrecan/death) - Managing go application shutdown with signals.|
|63|3|0|* [gotenv](https://github.com/subosito/gotenv) - Load environment variables from `.env` or any `io.Reader` in Go.|
|54|3|1|* [onecache](https://github.com/adelowo/onecache) - Caching library with support for multiple backend stores (Redis, Memcached, filesystem etc).|
|52|12|0|* [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) - XML Sitemap generator written in Go.|
|51|19|1|* [goreq](https://github.com/smallnest/goreq) - Enhanced simplified HTTP client based on gorequest.|
|51|2|0|* [netbug](https://github.com/e-dard/netbug) - Easy remote profiling of your services.|
|49|7|3|* [pm](https://github.com/VividCortex/pm) - Process (i.e. goroutine) manager with an HTTP API.|
|48|0|2|* [multitick](https://github.com/VividCortex/multitick) - Multiplexor for aligned tickers.|
|45|5|0|* [jsonf](https://github.com/miolini/jsonf) - Console tool for highlighted formatting and struct query fetching JSON.|
|43|1|3|* [xferspdy](https://github.com/monmohan/xferspdy) - Xferspdy provides binary diff and patch library in golang.|
|42|10|2|* [kazaam](https://github.com/Qntfy/kazaam) - API for arbitrary transformation of JSON documents.|
|32|0|0|* [abutil](https://github.com/bahlo/abutil) - Collection of often-used Golang helpers.|
|30|1|3|* [goback](https://github.com/carlescere/goback) - Go simple exponential backoff package.|
|30|9|11|* [golog](https://github.com/mlimaloureiro/golog) - Easy and lightweight CLI tool to time track your tasks.|
|26|3|0|* [util](https://github.com/shomali11/util) - Collection of useful utility functions. (strings, concurrency, manipulations, ...).|
|26|0|24|* [retry](https://github.com/kamilsk/retry) - Functional mechanism based on context to perform actions repetitively until successful.|
|25|3|0|* [go-astitodo](https://github.com/asticode/go-astitodo) - Parse TODOs in your GO code.|
|23|2|0|* [golarm](https://github.com/msempere/golarm) - Fire alarms with system events.|
|21|1|1|* [mp](https://github.com/sanbornm/mp) - Simple cli email parser. It currently takes stdin and outputs JSON.|
|20|2|8|* [copy-pasta](https://github.com/jutkko/copy-pasta) - Universal multi-workstation clipboard that uses S3 like backend for the storage.|
|18|2|2|* [rclient](https://github.com/zpatrick/rclient) - Readable, flexible, simple-to-use client for REST APIs.|
|17|0|0|* [gpath](https://github.com/tenntenn/gpath) - Library to simplify access struct fields with Go's expression in reflection.|
|14|4|1|* [goplaceholder](https://github.com/michiwend/goplaceholder) - a small golang lib to generate placeholder images.|
|14|0|0|* [mssqlx](https://github.com/linxGnu/mssqlx) - HA client for master slave (or master master) database which integrates simple, lightweight round-robin balancer. Based on sqlx.|
|13|2|0|* [ugo](https://github.com/alxrm/ugo) - ugo is slice toolbox with concise syntax for Go.|
|11|2|0|* [okrun](https://github.com/xta/okrun) - go run error steamroller.|
|9|0|0|* [go-httpheader](https://github.com/mozillazg/go-httpheader) - Go library for encoding structs into Header fields.|
|8|0|1|* [intrinsic](https://github.com/mengzhuo/intrinsic) - Use x86 SIMD without writing any assembly code.|
|8|1|0|* [filler](https://github.com/yaronsumel/filler) - small utility to fill structs using "fill" tag.|
|7|0|0|* [goxlsxwriter](https://github.com/fterrag/goxlsxwriter) - Golang bindings for libxlsxwriter for writing XLSX (Microsoft Excel) files.|
|7|2|1|* [rerate](https://github.com/abo/rerate) - Redis-based rate counter and rate limiter for Go.|
|6|2|0|* [generate](https://github.com/go-playground/generate) - runs go generate recursively on a specified path or environment variable and can filter by regex.|
|6|0|0|* [dlog](https://github.com/kirillDanshin/dlog) - Compile-time controlled logger to make your release smaller without removing debug calls.|
|6|1|0|* [command](https://github.com/txgruppi/command) - Command pattern for Go with thread safe serial and parallel dispatcher.|
|6|2|0|* [fastlz](https://github.com/digitalcrab/fastlz) - Wrap over [FastLz](http://fastlz.org/) (free, open-source, portable real-time compression library) for GoLang.|
|6|2|0|* [toolbox](https://github.com/viant/toolbox) - Slice, map, multimap, struct, function, data conversion utilities. Service router, macro evaluator, tokenizer.|
|4|1|0|* [go-respond](https://github.com/nicklaw5/go-respond) - Go package for handling common HTTP JSON responses.|
|4|1|0|* [jsonhal](https://github.com/RichardKnop/jsonhal) - Simple Go package to make custom structs marshal into HAL compatible JSON responses.|
|3|1|0|* [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - Go bindings based on the JSON API errors reference.|
|1|1|0|* [goseaweedfs](https://github.com/linxGnu/goseaweedfs) - SeaweedFS client library with almost full features.|
|0|0|0|* [robustly](https://github.com/VividCortex/robustly) - Runs functions resiliently, catching and restarting panics.|
|0|0|0|* [lrserver](https://github.com/jaschaephraim/lrserver) - LiveReload server for Go.|

*Libraries for validation.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|2024|195|41|* [govalidator](https://github.com/asaskevich/govalidator) - Validators and sanitizers for strings, numerics, slices and structs.|
|1137|88|8|* [validator](https://github.com/go-playground/validator) - Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving.|
|417|22|0|* [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) - Supports validation of various data types (structs, strings, maps, slices, etc.) with configurable and extensible validation rules specified in usual code constructs instead of struct tags.|
|14|6|0|* [validate](https://github.com/markbates/validate) - This package provides a framework for writing validations for Go applications.|

*Libraries for version control.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|1033|188|37|* [git2go](https://github.com/libgit2/git2go) - Go bindings for libgit2.|
|50|12|19|* [go-vcs](https://github.com/sourcegraph/go-vcs) - manipulate and inspect VCS repositories in Go.|
|49|5|2|* [gh](https://github.com/rjeczalik/gh) - Scriptable server and net/http middleware for GitHub Webhooks.|
|9|2|0|* [hgo](https://github.com/beyang/hgo) - Hgo is a collection of Go packages providing read-access to local Mercurial repositories.|

*Libraries for manipulating video.*


|stars|forks|issues|description|
| --- | --- | --- | --- |
|349|68|15|* [goav](https://github.com/giorgisio/goav) - Comphrensive Go bindings for FFmpeg.|
|297|68|22|* [gmf](https://github.com/3d0c/gmf) - Go bindings for FFmpeg av\* libraries.|
|132|26|10|* [gst](https://github.com/ziutek/gst) - Go bindings for GStreamer.|
|24|1|1|* [go-astisub](https://github.com/asticode/go-astisub) - Manipulate subtitles in GO (.srt, .stl, .ttml, .webvtt, .ssa/.ass, teletext, .smi, etc.).|
|11|0|0|* [v4l](https://github.com/korandiz/v4l) - Video capture library for Linux, written in Go.|
|3|0|0|* [libgosubs](https://github.com/wargarblgarbl/libgosubs) - Subtitle format support for go. Supports .srt, .ttml, and .ass.|

*Full stack web frameworks.*

* [aah](https://aahframework.org) - Scalable, performant, rapid development Web framework for Go.
* [Buffalo](http://gobuffalo.io) - Bringing the productivity of Rails to Go!
* [REST Layer](http://rest-layer.io) - Framework to build REST/GraphQL API on top of databases with mostly configuration over code.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|12169|2801|312|* [Beego](https://github.com/astaxie/beego) - beego is an open-source, high-performance web framework for the Go programming language.|
|11562|1355|114|* [Gin](https://github.com/gin-gonic/gin) - Gin is a web framework written in Go! It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity.|
|8729|1158|51|* [Revel](https://github.com/revel/revel) - High-productivity web framework for the Go language.|
|8143|712|84|* [Echo](https://github.com/labstack/echo) - High performance, minimalist Go web framework.|
|2883|313|33|* [go-json-rest](https://github.com/ant0ine/go-json-rest) - Quick and easy way to setup a RESTful JSON API.|
|2267|225|52|* [goa](https://github.com/raphael/goa) - Framework for developing microservices based on the design of Ruby's Praxis.|
|2016|184|12|* [Macaron](https://github.com/go-macaron/macaron) - Macaron is a high productive and modular design web framework in Go.|
|1916|111|5|* [utron](https://github.com/gernest/utron) - Lightweight MVC framework for Go(Golang).|
|1894|121|6|* [Gizmo](https://github.com/NYTimes/gizmo) - Microservice toolkit used by the New York Times.|
|955|77|27|* [tigertonic](https://github.com/rcrowley/go-tigertonic) - Go framework for building JSON web services inspired by Dropwizard.|
|618|90|9|* [tango](https://github.com/lunny/tango) - Micro & pluggable web framework for Go.|
|514|20|0|* [traffic](https://github.com/pilu/traffic) - Sinatra inspired regexp/pattern mux and web framework for Go.|
|379|10|0|* [gongular](https://github.com/mustafaakin/gongular) - Fast Go web framework with input mapping/validation and (DI) Dependency Injection.|
|317|30|3|* [neo](https://github.com/ivpusic/neo) - Neo is minimal and fast Go Web Framework with extremely simple API.|
|311|34|10|* [mango](https://github.com/paulbellamy/mango) - Mango is a modular web-application framework for Go, inspired by Rack, and PEP333.|
|306|20|8|* [Gondola](https://github.com/rainycape/gondola) - The web framework for writing faster sites, faster.|
|143|6|0|* [go-relax](https://github.com/codehack/go-relax) - Framework of pluggable components to build RESTful API's.|
|142|31|0|* [Gem](https://github.com/go-gem/gem) - Simple and fast web framework, friendly to REST API.|
|139|19|0|* [Zerver](https://github.com/cosiner/zerver) - Zerver is an expressive, modular, feature completed RESTful framework.|
|137|13|5|* [Goat](https://github.com/bahlo/goat) - Minimalistic REST API server in Go.|
|104|11|2|* [go-rest](https://github.com/ungerik/go-rest) - Small and evil REST framework for Go.|
|71|5|3|* [violetear](https://github.com/nbari/violetear) - Go HTTP router.|
|43|4|1|* [Air](https://github.com/sheng/air) - Ideal RESTful web framework for Go.|
|38|2|1|* [YARF](https://github.com/yarf-framework/yarf) - Fast micro-framework designed to build REST APIs and web services in a fast and simple way.|
|34|5|0|* [Microservice](https://github.com/claygod/microservice) - The framework for the creation of microservices, written in Golang.|
|30|10|0|* [Florest](https://github.com/jabong/florest-core) - High-performance workflow based REST API framework.|
|24|2|0|* [Fireball](https://github.com/zpatrick/fireball) - More "natural" feeling web framework.|
|13|0|0|* [rex](https://github.com/goanywhere/rex) - Rex is a library for modular development built upon gorilla/mux, fully compatible with `net/http`.|
|1|0|0|* [sawsij](https://github.com/jaybill/sawsij) - lightweight, open-source web framework for building high-performance, data-driven web applications.|
|0|0|0|* [Resoursea](https://github.com/resoursea/api) - REST framework for quickly writing resource based services.|
|0|0|0|* [Golf](https://github.com/dinever/golf) - Golf is a fast, simple and lightweight micro-web framework for Go. It comes with powerful features and has no dependencies other than the Go Standard Library.|

#### Actual middlewares


|stars|forks|issues|description|
| --- | --- | --- | --- |
|586|61|7|* [Tollbooth](https://github.com/didip/tollbooth) - Rate limit HTTP request handler.|
|60|9|1|* [XFF](https://github.com/sebest/xff) - Handle `X-Forwarded-For` header and friends.|
|25|0|0|* [formjson](https://github.com/rs/formjson) - Transparently handle JSON input as a standard form POST.|
|0|0|0|* [CORS](https://github.com/rs/cors) - Easily add CORS capabilities to your API.|
|0|0|0|* [Limiter](https://github.com/ulule/limiter) - Dead simple rate limit middleware for Go.|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|4913|392|7|* [negroni](https://github.com/urfave/negroni) - Idiomatic HTTP middleware for Golang.|
|1333|85|3|* [alice](https://github.com/justinas/alice) - Painless middleware chaining for Go.|
|936|80|0|* [render](https://github.com/unrolled/render) - Go package for easily rendering JSON, XML, and HTML template responses.|
|431|28|5|* [stats](https://github.com/thoas/stats) - Go middleware that stores various information about your web application.|
|275|16|1|* [interpose](https://github.com/carbocation/interpose) - Minimalist net/http middleware for golang.|
|200|7|0|* [muxchain](https://github.com/stephens2424/muxchain) - Lightweight middleware for net/http.|
|80|1|0|* [Volatile](https://github.com/volatile/core) - Minimalist middleware stack promoting flexibility, good practices and clean code.|
|63|1|0|* [chain](https://github.com/codemodus/chain) - Handler wrapper chaining with scoped data (net/context-based "middleware").|
|57|2|0|* [gores](https://github.com/alioygur/gores) - Go package that handles HTML, JSON, XML and etc. responses. Useful for RESTful APIs.|
|57|4|1|* [rye](https://github.com/InVisionApp/rye) - Tiny Go middleware library (with canned Middlewares) that supports JWT, CORS, Statsd, and Go 1.7 context.|
|52|4|0|* [go-wrap](https://github.com/go-on/wrap) - Small middlewares package for net/http.|
|6|0|0|* [catena](https://github.com/codemodus/catena) - http.Handler wrapper catenation (same API as "chain").|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|5473|546|43|* [httprouter](https://github.com/julienschmidt/httprouter) - High performance router. Use this and the standard http handlers to form a very high performance web framework.|
|4417|596|24|* [mux](https://github.com/gorilla/mux) - Powerful URL router and dispatcher for golang.|
|2403|156|5|* [chi](https://github.com/go-chi/chi) - Small, fast and expressive HTTP router built on net/context.|
|1232|91|17|* [gocraft/web](https://github.com/gocraft/web) - Mux and middleware package in Go.|
|1062|103|6|* [pat](https://github.com/bmizerany/pat) - Sinatra style pattern muxer for Go’s net/http library, by the author of Sinatra.|
|1052|71|1|* [Bone](https://github.com/go-zoo/bone) - Lightning Fast HTTP Multiplexer.|
|515|32|4|* [Goji](https://github.com/goji/goji) - Goji is a minimalistic and flexible HTTP request multiplexer with support for `net/context`.|
|345|52|5|* [fasthttprouter](https://github.com/buaazp/fasthttprouter) - High performance router forked from `httprouter`. The first router fit for `fasthttp`.|
|341|11|5|* [Siesta](https://github.com/VividCortex/siesta) - Composable framework to write middleware and handlers.|
|256|26|1|* [httptreemux](https://github.com/dimfeld/httptreemux) - High-speed, flexible tree-based HTTP router for Go. Inspiration from httprouter.|
|205|34|6|* [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) - An extremely fast Go (golang) HTTP router that supports regular expression route matching. Comes with full support for building RESTful APIs.|
|171|22|10|* [vestigo](https://github.com/husobee/vestigo) - Performant, stand-alone, HTTP compliant URL Router for go web applications.|
|126|7|0|* [gowww/router](https://github.com/gowww/router) - Lightning fast HTTP router fully compatible with the net/http.Handler interface.|
|108|12|2|* [zeus](https://github.com/daryl/zeus) - Very simple and fast HTTP router for Go.|
|82|5|0|* [alien](https://github.com/gernest/alien) - Lightweight and fast http router from outer space.|
|75|2|0|* [Bxog](https://github.com/claygod/Bxog) - Simple and fast HTTP router for Go. It works with routes of varying difficulty, length and nesting. And he knows how to create a URL from the received parameters.|
|17|1|1|* [medeina](https://github.com/imdario/medeina) - Medeina is a HTTP routing tree based on HttpRouter, inspired by Roda and Cuba.|
|15|1|0|* [GoRouter](https://github.com/vardius/gorouter) - GoRouter is a Server/API micro framwework, HTTP request router, multiplexer, mux that provides request router with middleware supporting `net/context`.|
|0|0|0|* [lars](https://github.com/go-playground/lars) - Is a lightweight, fast and extensible zero allocation HTTP router for Go used to create customizable frameworks.|
|0|0|0|* [pure](https://github.com/go-playground/pure) - Is a lightweight HTTP router that sticks to the std "net/http" implementation.|
|0|0|0|* [xmux](https://github.com/rs/xmux) - High performance muxer based on `httprouter` with `net/context` support.|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|319|68|32|* [go-ole](https://github.com/go-ole/go-ole) - Win32 OLE implementation for golang.|
|54|1|0|* [d3d9](https://github.com/gonutz/d3d9) - Go bindings for Direct3D9.|

*Libraries and tools for manipulating XML.*


# Tools

*Go software and plugins.*

|stars|forks|issues|description|
| --- | --- | --- | --- |
|122|32|5|* [go-pkg-xmlx](https://github.com/jteeuwen/go-pkg-xmlx) - Extension to the standard Go XML package. Maintains a node tree that allows forward/backwards browsing and exposes some simple single/multi-node search functions.|
|73|11|0|* [xquery](https://github.com/antchfx/xquery) - XQuery lets you extract data from HTML/XML documents using XPath expression.|
|27|3|2|* [xpath](https://github.com/antchfx/xpath) - XPath package for Go.|
|6|5|9|* [XML-Comp](https://github.com/xml-comp/xml-comp) - Simple command line XML comparer that generates diffs of folders, files and tags.|
|0|0|0|* [xmlwriter](https://github.com/shabbyrobe/xmlwriter) - Procedural XML generation API based on libxml2's xmlwriter module.|

* [GoCover.io](http://gocover.io/) - GoCover.io offers the code coverage of any golang package as a service.
* [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) - Tool to fix (add, remove) your Go imports automatically.
* [Golint online](http://go-lint.appspot.com/) - Lints online Go source files on GitHub, Bitbucket and Google Project Hosting using the golint package.
* [goreturns](https://sourcegraph.com/github.com/sqs/goreturns) - Adds zero-value return statements to match the func return types.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|1972|240|72|* [GoLint](https://github.com/golang/lint) - Golint is a linter for Go source code.|
|1867|142|14|* [Go Metalinter](https://github.com/alecthomas/gometalinter) - Metalinter is a tool to automatically apply all static analysis tool and report their output in normalized form.|
|867|50|9|* [errcheck](https://github.com/kisielk/errcheck) - Errcheck is a program for checking for unchecked errors in Go programs.|
|717|49|8|* [gcvis](https://github.com/davecheney/gcvis) - Visualise Go program GC trace data in real time.|
|659|10|2|* [interfacer](https://github.com/mvdan/interfacer) - Linter that suggests interface types.|
|210|10|1|* [gostatus](https://github.com/shurcooL/gostatus) - Command line tool, shows the status of repositories that contain Go packages.|
|183|17|1|* [goast-viewer](https://github.com/yuroyoro/goast-viewer) - Web based Golang AST visualizer.|
|178|8|9|* [unconvert](https://github.com/mdempsky/unconvert) - Remove unnecessary type conversions from Go source.|
|165|8|0|* [go-cleanarch](https://github.com/roblaszczak/go-cleanarch) - go-cleanarch was created to validate Clean Architecture rules, like a The Dependency Rule and interaction between packages in your Go projects.|
|107|2|5|* [apicompat](https://github.com/bradleyfalzon/apicompat) - Checks recent changes to a Go project for backwards incompatible changes.|
|88|4|2|* [dupl](https://github.com/mibk/dupl) - Tool for code clone detection.|
|61|10|1|* [validate](https://github.com/mccoyst/validate) - Automatically validates struct fields with tags.|
|55|8|4|* [go-checkstyle](https://github.com/qiniu/checkstyle) - checkstyle is a style check tool like java checkstyle. This tool inspired by java checkstyle, golint. The style refered to some points in Go Code Review Comments.|
|53|5|1|* [lint](https://github.com/surullabs/lint) - Run linters as part of go test.|
|34|1|0|* [go-outdated](https://github.com/firstrow/go-outdated) - Console application that displays outdated packages.|
|0|0|0|* [gosimple](https://github.com/dominikh/go-tools/tree/master/cmd/gosimple) - gosimple is a linter for Go source code that specialises on simplifying code.|
|0|0|0|* [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) - staticcheck is `go vet` on steroids, applying a ton of static analysis checks you might be used to from tools like ReSharper for C#.|
|0|0|0|* [unused](https://github.com/dominikh/go-tools/tree/master/cmd/unused) - unused checks Go code for unused constants, variables, functions and types.|

* [Go plugin for JetBrains IDEs](https://plugins.jetbrains.com/plugin/9568-go) - Go plugin for JetBrains IDEs.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|7101|709|39|* [vim-go](https://github.com/fatih/vim-go) - Go development plugin for Vim.|
|3855|457|46|* [gocode](https://github.com/nsf/gocode) - Autocompletion daemon for the Go programming language.|
|2775|276|129|* [vscode-go](https://github.com/Microsoft/vscode-go) - Extension for Visual Studio Code (VS Code) which provides support for the Go language.|
|2683|242|215|* [GoSublime](https://github.com/DisposaBoy/GoSublime) - Golang plugin collection for the text editor SublimeText 2 providing code completion and other IDE-like features.|
|1283|105|75|* [go-plus](https://github.com/joefitzgerald/go-plus) - Go (Golang) Package For Atom That Adds Autocomplete, Formatting, Syntax Checking, Linting and Vetting.|
|710|220|39|* [Goclipse](https://github.com/GoClipse/goclipse) - Eclipse plugin for Go.|
|640|118|38|* [go-mode](https://github.com/dominikh/go-mode.el) - Go mode for GNU/Emacs.|
|136|17|7|* [Watch](https://github.com/eaburns/Watch) - Runs a command in an acme win on file changes.|
|73|18|0|* [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) - Vim plugin to highlight syntax errors on save.|
|14|2|7|* [velour](https://github.com/velour/velour) - IRC client for the acme editor.|
|0|0|0|* [go-lang-idea-plugin](https://github.com/go-lang-plugin-org/go-lang-idea-plugin) (deprecated) - The previous Go plugin for IntelliJ (JetBrains) IDEA, now replaced by the official plugin (above).|

* [gb](https://getgb.io/) - An easy to use project based build tool for the Go programming language.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|2291|169|26|* [OctoLinker](https://github.com/OctoLinker/browser-extension) - Navigate through go files efficiently with the OctoLinker browser extension for GitHub.|
|1441|295|214|* [go-swagger](https://github.com/go-swagger/go-swagger) - Swagger 2.0 implementation for go. Swagger is a simple yet powerful representation of your RESTful API.|
|890|28|4|* [go-callvis](https://github.com/TrueFurby/go-callvis) - Visualize call graph of your Go program using dot format.|
|158|4|1|* [depth](https://github.com/KyleBanks/depth) - Visualize dependency trees of any package by analyzing imports.|
|137|4|0|* [rts](https://github.com/galeone/rts) - RTS: response to struct. Generates Go structs from server responses.|
|83|6|2|* [colorgo](https://github.com/songgao/colorgo) - Wrapper around `go` command for colorized `go build` output.|
|30|5|4|* [go-pkg-complete](https://github.com/skelterjohn/go-pkg-complete) - Bash completion for go and wgo.|

*Software written in Go.*

### DevOps Tools

* [Gogs](https://gogs.io/) - A Self Hosted Git Service in the Go Programming Language.
* [Wide](https://wide.b3log.org/login) - Web-based IDE for Teams using Golang.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|45290|13462|2878|* [Moby](https://github.com/moby/moby) - Collaborative project for the container ecosystem to assemble container-based systems.|
|26536|9469|5316|* [kubernetes](https://github.com/kubernetes/kubernetes) - Container Cluster Manager from Google.|
|6821|1777|303|* [Packer](https://github.com/mitchellh/packer) - Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.|
|6232|367|38|* [Vegeta](https://github.com/tsenart/vegeta) - HTTP load testing tool and library. It's over 9000!|
|3488|377|514|* [Gitea](https://github.com/go-gitea/gitea) - Fork of Gogs, entirely community driven.|
|2993|193|117|* [GVM](https://github.com/moovweb/gvm) - GVM provides an interface to manage Go versions.|
|2342|390|359|* [bosun](https://github.com/bosun-monitor/bosun) - Time Series Alerting Framework.|
|2298|156|32|* [gox](https://github.com/mitchellh/gox) - Dead simple, no frills Go cross compile tool.|
|1980|155|26|* [Hey](https://github.com/rakyll/hey) - Hey is a tiny program that sends some load to a web application.|
|1914|141|11|* [webhook](https://github.com/adnanh/webhook) - Tool which allows user to create HTTP endpoints (hooks) that execute commands on the server.|
|1662|297|53|* [Go Metrics](https://github.com/rcrowley/go-metrics) - Go port of Coda Hale's Metrics library: https://github.com/codahale/metrics.|
|1455|63|8|* [goxc](https://github.com/laher/goxc) - build tool for Go, with a focus on cross-compiling and packaging.|
|1398|179|150|* [aptly](https://github.com/smira/aptly) - aptly is a Debian repository management tool.|
|1058|79|17|* [kala](https://github.com/ajvb/kala) - Simplistic, modern, and performant job scheduler.|
|844|113|35|* [s3gof3r](https://github.com/rlmcpherson/s3gof3r) - Small utility/library optimized for high speed transfer of large objects into and out of Amazon S3.|
|829|76|15|* [Banshee](https://github.com/eleme/banshee) - Anomalies detection system for periodic metrics.|
|799|70|11|* [StatusOK](https://github.com/sanathp/statusok) - Monitor your Website and REST APIs.Get Notified through Slack, E-mail when your server is down or response time is more than expected.|
|668|25|1|* [bombardier](https://github.com/codesenberg/bombardier) - Fast cross-platform HTTP benchmarking tool.|
|511|54|7|* [go-selfupdate](https://github.com/sanbornm/go-selfupdate) - Enable your Go applications to self update.|
|342|37|35|* [Scaleway-cli](https://github.com/scaleway/scaleway-cli) - Manage BareMetal Servers from Command Line (as easily as with Docker).|
|275|26|5|* [gonative](https://github.com/inconshreveable/gonative) - Tool which creates a build of Go that can cross compile to all platforms while still using the Cgo-enabled versions of the stdlib packages.|
|208|19|8|* [godbg](https://github.com/sirnewton01/godbg) - Web-based gdb front-end application.|
|206|31|0|* [aurora](https://github.com/Luxurioust/aurora) - Cross-platform web-based Beanstalkd queue server console.|
|145|11|0|* [ostent](https://github.com/ostrost/ostent) - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB.|
|143|27|2|* [dogo](https://github.com/liudng/dogo) - Monitoring changes in the source file and automatically compile and run (restart).|
|70|5|0|* [grapes](https://github.com/yaronsumel/grapes) - Lightweight tool designed to distribute commands over ssh with ease.|
|35|5|9|* [Dropship](https://github.com/chrismckenzie/dropship) - Tool for deploying code via cdn.|
|31|1|6|* [Rodent](https://github.com/alouche/rodent) - Rodent helps you manage Go versions, projects and track dependencies.|
|29|5|0|* [easyssh-proxy](https://github.com/appleboy/easyssh-proxy) - Golang package for easy remote execution through SSH and SCP downloading via `ProxyCommand`.|
|24|2|1|* [winrm-cli](https://github.com/masterzen/winrm-cli) - Cli tool to remotely execute commands on Windows machines.|
|11|3|0|* [awsenv](https://github.com/soniah/awsenv) - Small binary that loads Amazon (AWS) environment variables for a profile.|
|10|1|3|* [drone-scp](https://github.com/appleboy/drone-scp) - Copy files and artifacts via SSH using a binary, docker or Drone CI.|
|8|1|0|* [drone-jenkins](https://github.com/appleboy/drone-jenkins) - Trigger downstream Jenkins jobs using a binary, docker or Drone CI.|
|1|0|2|* [sg](https://github.com/ChristopherRabotin/sg) - Benchmarks a set of HTTP endpoints (like ab), with possibility to use the reponse code and data between each call for specific server stress based on its previous response.|
|0|0|0|* [Pewpew](https://github.com/bengadbois/pewpew) - Flexible HTTP command line stress tester.|
|0|0|0|* [gobrew](https://github.com/cryptojuice/gobrew) - gobrew lets you easily switch between multiple versions of go.|
|0|0|0|* [Mora](https://github.com/emicklei/mora) - REST server for accessing MongoDB documents and meta data.|
|0|0|0|* [govvv](https://github.com/ahmetalpbalkan/govvv) - “go build” wrapper to easily add version information into Go binaries.|
* [Docker](http://www.docker.com/) - Open platform for distributed applications for developers and sysadmins.
* [Gogland](https://jetbrains.com/go) - Full featured cross-platform Go IDE.
* [hugo](http://gohugo.io/) - Fast and Modern Static Website Engine.
* [Juju](https://jujucharms.com/) - Cloud-agnostic service deployment and orchestration - supports EC2, Azure, Openstack, MAAS and more.
* [limetext](http://limetext.org/) - Lime Text is a powerful and elegant text editor primarily developed in Go that aims to be a Free and open-source software successor to Sublime Text.
* [syncthing](https://syncthing.net/) - Open, decentralized file synchronization tool and protocol.
* [tsuru](https://tsuru.io/) - Extensible and open source Platform as a Service software.

# Resources

*Where to discover new Go libraries.*

|stars|forks|issues|description|
| --- | --- | --- | --- |
|7796|700|63|* [Gor](https://github.com/buger/gor) - Http traffic replication tool, for replaying traffic from production to stage/dev environments in real-time.|
|7327|710|467|* [rkt](https://github.com/coreos/rkt) - App Container runtime that integrates with init systems, is compatible with other container formats like Docker, and supports alternative execution engines like KVM.|
|4948|196|16|* [Comcast](https://github.com/tylertreat/Comcast) - Simulate bad network connections.|
|4568|622|31|* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Fast, Simple and Scalable Distributed File System with O(1) disk seek.|
|4130|683|61|* [confd](https://github.com/kelseyhightower/confd) - Manage local application configuration files using templates and data from etcd or consul.|
|3913|532|240|* [LiteIDE](https://github.com/visualfc/liteide) - LiteIDE is a simple, open source, cross-platform Go IDE.|
|2809|242|2|* [nes](https://github.com/fogleman/nes) - Nintendo Entertainment System (NES) emulator written in Go.|
|2450|203|183|* [restic](https://github.com/restic/restic) - De-duplicating backup program.|
|2400|312|106|* [fleet](https://github.com/coreos/fleet) - Distributed init System.|
|2095|111|25|* [toxiproxy](https://github.com/shopify/toxiproxy) - Proxy to simulate network and system conditions for automated tests.|
|1838|134|11|* [myLG](https://github.com/mehrdadrad/mylg) - Command Line Network Diagnostic tool written in Go.|
|1566|231|131|* [snap](https://github.com/intelsdi-x/snap) - Powerful telemetry framework.|
|1551|137|8|* [Circuit](https://github.com/gocircuit/circuit) - Circuit is a programmable platform-as-a-service (PaaS) and/or Infrastructure-as-a-Service (IaaS), for management, discovery, synchronization and orchestration of services and hosts comprising cloud applications.|
|1513|58|28|* [Stack Up](https://github.com/pressly/sup) - Stack Up, a super simple deployment tool - just Unix - think of it like 'make' for a network of servers.|
|1275|36|10|* [borg](https://github.com/crufter/borg) - Terminal based search engine for bash snippets.|
|779|25|8|* [Go Package Store](https://github.com/shurcooL/Go-Package-Store) - App that displays updates for the Go packages in your GOPATH.|
|510|33|11|* [Leaps](https://github.com/jeffail/leaps) - Pair programming service using Operational Transforms.|
|421|57|17|* [peg](https://github.com/pointlander/peg) - Peg, Parsing Expression Grammar, is an implementation of a Packrat parser generator.|
|329|36|2|* [mockingjay](https://github.com/quii/mockingjay-server) - Fake HTTP servers and consumer driven contracts from one configuration file. You can also make the server randomly misbehave to help do more realistic performance tests.|
|261|33|7|* [Documize](https://github.com/documize/community) - Modern wiki software that integrates data from SaaS tools.|
|248|15|17|* [wellington](https://github.com/wellington/wellington) - Sass project management tool, extends the language with sprite functions (like Compass).|
|243|30|4|* [vFlow](https://github.com/VerizonDigital/vflow) - High-performance, scalable and reliable IPFIX, sFlow and Netflow collector.|
|198|29|7|* [ipe](https://github.com/dimiro1/ipe) - Open source Pusher server implementation compatible with Pusher client libraries written in GO.|
|163|15|13|* [Tenyks](https://github.com/kyleterry/tenyks) - Service oriented IRC bot using Redis and JSON for messaging.|
|154|5|1|* [orange-cat](https://github.com/noraesae/orange-cat) - Markdown previewer written in Go.|
|136|19|1|* [shell2http](https://github.com/msoap/shell2http) - Executing shell commands via http server (for prototyping or remote control).|
|132|17|0|* [Cherry](https://github.com/rafael-santiago/cherry) - Tiny webchat server in Go.|
|128|9|13|* [gocc](https://github.com/goccmack/gocc) - Gocc is a compiler kit for Go written in Go.|
|60|7|0|* [boxed](https://github.com/tejo/boxed) - Dropbox based blog engine.|
|37|7|4|* [websysd](https://github.com/ian-kent/websysd) - Web based process manager (like Marathon or Upstart).|
|27|1|0|* [DDNS](https://github.com/skibish/ddns) - Personal DDNS client with Digital Ocean Networking DNS as backend.|
|18|4|0|* [toto](https://github.com/blogcin/ToTo) - Simple proxy server written in Go language, can be used together with browser.|
|11|0|0|* [naclpipe](https://github.com/unix4fun/naclpipe) - Simple NaCL EC25519 based crypto pipe tool written in Go.|
|10|0|0|* [GoDocTooltip](https://github.com/diankong/GoDocTooltip) - Chrome extension for Go Doc sites, which shows function description as tooltip at funciton list.|
|7|1|0|* [JayDiff](https://github.com/yazgazan/jaydiff) - JSON diff utility written in Go.|
|0|0|0|* [Postman](https://github.com/zachlatta/postman) - Command-line utility for batch-sending email.|
|0|0|0|* [Orbit](https://github.com/gulien/orbit) - A simple tool for running commands and generating files from templates.|


|stars|forks|issues|description|
| --- | --- | --- | --- |
|945|127|21|* [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) - Go HTTP request router benchmark and comparison.|
|780|107|32|* [skynet](https://github.com/atemerev/skynet) - Skynet 1M threads microbenchmark.|
|540|57|4|* [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) - Benchmarks of Go serialization methods.|
|509|62|2|* [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - Go web framework benchmark.|
|111|10|1|* [speedtest-resize](https://github.com/fawick/speedtest-resize) - Compare various Image resize algorithms for the Go language.|
|83|24|2|* [autobench](https://github.com/davecheney/autobench) - Framework to compare the performance between different Go versions.|
|71|11|0|* [go-benchmarks](https://github.com/tylertreat/go-benchmarks) - Few miscellaneous Go microbenchmarks. Compare some language features to alternative approaches.|
|67|6|1|* [gospeed](https://github.com/feyeleanor/GoSpeed) - Go micro-benchmarks for calculating the speed of language constructs.|
|46|2|0|* [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) - Benchmarks of common basic operations for the Go language.|
|31|4|1|* [golang-sql-benchmark](https://github.com/tyler-smith/golang-sql-benchmark) - Collection of benchmarks for popular Go database/SQL utilities.|
|11|0|0|* [kvbench](https://github.com/jimrobinson/kvbench) - Key/Value database benchmark.|
|11|0|0|* [golang-micro-benchmarks](https://github.com/amscanne/golang-micro-benchmarks) - Tiny collection of Go micro benchmarks. The intent is to compare some language features to others.|
|7|0|0|* [go-benchmark-app](https://github.com/mrLSD/go-benchmark-app) - Powerful HTTP-benchmark tool mixed with Аb, Wrk, Siege tools. Gathering statistics and various parameters for benchmarks and comparison results.|
|4|0|0|* [go-type-assertion-benchmark](https://github.com/hgfischer/go-type-assertion-benchmark) - Naive performance test of two ways to do type assertion in Go.|

* [Capital Go](http://www.capitalgolang.com) - Washington, D.C., USA
* [dotGo](http://www.dotgo.eu) - Paris, France
* [GoCon](http://gocon.connpass.com/) - Tokyo, Japan
* [GolangUK](http://golanguk.com/) - London, UK
* [GopherChina](http://gopherchina.org) - Shanghai, China
* [GopherCon](http://www.gophercon.com/) - Denver, USA
* [GopherCon Brazil](https://gopherconbr.org) - Florianópolis, BR
* [GopherCon Dubai](http://www.gophercon.ae/) - Dubai, UAE
* [GopherCon India](http://www.gophercon.in/) - Pune, India
* [GopherCon Singapore](https://gophercon.sg) - Mapletree Business City, Singapore
* [GothamGo](http://gothamgo.com/) - New York City, USA

## E-Books

* [A Go Developer's Notebook](https://leanpub.com/GoNotebook/read)
* [An Introduction to Programming in Go](http://www.golang-book.com/)
* [Build Web Application with Golang](https://www.gitbook.com/book/astaxie/build-web-application-with-golang/details)
* [Building Web Apps With Go](https://www.gitbook.com/book/codegangsta/building-web-apps-with-go/details)
* [Go Bootcamp](http://golangbootcamp.com)
* [Learning Go](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
* [Network Programming With Go](https://jan.newmarch.name/go/)
* [The Go Programming Language](http://www.gopl.io/)
* [Web Application with Go the Anti-Textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/)

|stars|forks|issues|description|
| --- | --- | --- | --- |
|3865|460|2|* [GoBooks](https://github.com/dariubs/GoBooks) - A curated list of Go books.|

* [@golang](https://twitter.com/golang)
* [@golang_news](https://twitter.com/golang_news)
* [@golangflow](https://twitter.com/golangflow)
* [@golangweekly](https://twitter.com/golangweekly)

## Websites

* [Awesome Go @LibHunt](https://go.libhunt.com) - Your go-to Go Toolbox.
* [Flipboard - Go Magazine](https://flipboard.com/section/the-golang-magazine-bVP7nS) - Collection of Go articles and tutorials.
* [Go Blog](http://blog.golang.org) - The official Go blog.
* [Go Challenge](http://golang-challenge.org/) - Learn Go by solving problems and getting feedback from Go experts.
* [Go Forum](https://forum.golangbridge.org) - Forum to discuss Go.
* [Go In 5 Minutes](https://www.goin5minutes.com/) - 5 minute screencasts focused on getting one thing done.
* [godoc.org](https://godoc.org/) - Documentation for open source Go packages.
* [Golang Flow](http://golangflow.io) - Post Updates, News, Packages and more.
* [Golang News](https://golangnews.com) - Links and news about Go programming.
* [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - Go mailing list.
* [Google Plus Community](https://plus.google.com/communities/114112804251407510571) - The Google+ community for #golang enthusiasts.
* [gowalker.org](https://gowalker.org) - Go Project API documentation.
* [r/Golang](https://www.reddit.com/r/golang) - News about Go.

|stars|forks|issues|description|
| --- | --- | --- | --- |
|19553|2498|0|* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - List of other amazingly awesome lists.|
|9797|911|8|* [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - Curated list of awesome remote jobs. A lot of them is looking for Go hackers.|
|114|7|0|* [golang-graphics](https://github.com/mholt/golang-graphics) - Collection of Go images, graphics, and art.|
|24|0|0|* [gocryforhelp](https://github.com/ninedraft/gocryforhelp) - Collection of Go projects that needs help. Good place to start your open-source way in Go.|
|0|0|0|* [Go Projects](https://github.com/golang/go/wiki/Projects) - List of projects on the Go community wiki.|
|0|0|0|* [Trending Go repositories on GitHub today](https://github.com/trending?l=go) - Good place to find new Go libraries.|

* [A Tour of Go](http://tour.golang.org/) - Interactive tour of Go.
* [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - Get familiar with Gin and find out how it can help you reduce boilerplate code and build a request handling pipeline.
* [Go By Example](https://gobyexample.com/) - Hands-on introduction to Go using annotated example programs.
* [Go database/sql tutorial](http://go-database-sql.org/) - Introduction to database/sql.
* [Golangbot](https://golangbot.com/learn-golang-series/) - Tutorials to get started with programming in Go.
* [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - Get started with Godog — a Behavior-driven development framework for building and testing Go applications.
