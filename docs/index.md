

### Contents

- [Learning](#learning)
- [HLS](#hls)
- [DASH](#dash)
- [Encoding](#encoding)
- [Reading](#reading)
- [Specs & Standards](#specs-standards)
- [Players](#players)
- [FFMPEG](#ffmpeg)
- [Audio](#audio)
- [Subtitles & Closed Captions](#subtitle-cc)
- [HEVC](#hevc)
- [Ads](#ads)
- [Roku](#roku)
- [Dolby](#dolby)
- [QoE & Analytics](#qoe)
- [Tools](#tools)
- [DRM](#drm)
- [Testing](#testing)
- [Talks & Presentations](#talks)
- [Books](#books)
- [CDN](#cdn)

## Learning
*An awesome list of learning video streaming resources.*

* [A short history of video coding](https://www.slideshare.net/vcodex/a-short-history-of-video-coding?from_m_app=ios)  - From H.261 to H.265
* [Adding Alternate Media to a Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/adding_alternate_media_to_a_playlist)  - 
* [Back to Basics: Encoding Definition and Adaptive Bitrate](https://bitmovin.com/encoding-definition-bitrates/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz-8MPFxhR7snQrxPYM7Bl3UTEMgOh5ZXoDQCHjLl9lkskqE0IfBhEuz3us39Br-lvA_CnyNmQl6L5wqO6iKOfAJ8HznenQ&_hsmi=79678208&utm_content=79677632&utm_source=hs_email&hsCtaTracking=b8eb0e0a-f292-435e-8b99-719b75d81412%7C367afa65-d810-4c2e-aa2c-c87e897a8942)  - 
* [Create your own video streaming server with Linux | Opensource.com](https://opensource.com/article/19/1/basic-live-video-streaming-server)  - 
* [Creating A Production Ready Multi Bitrate HLS VOD stream](https://docs.peer5.com/guides/production-ready-hls-vod/)  - 
* [Creating a Master Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/creating_a_master_playlist#overview)  - 
* [Eyevinn/streaming-onboarding: New to streaming and don't know where to start? This is the place for you!](https://github.com/Eyevinn/streaming-onboarding)  - 
* [FFmpeg and how to use it wrong | VideoBlerg](https://videoblerg.wordpress.com/2017/11/10/ffmpeg-and-how-to-use-it-wrong/)  - 
* [Generate MPEG-TS from file with ffmpeg](https://medium.com/@eyevinntechnology/generate-mpeg-ts-from-file-with-ffmpeg-7561181e6369?source=userActivityShare-94bccb50d11-1560983471&_branch_match_id=670020142756633081)  - 
* [Guide to Mobile Video Streaming with HLS](http://mux.com/blog/mobile-hls-guide/)  - 
* [HLS Authoring Specification for Apple Devices | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - 
* [HLS adaptive streaming tutorial with CloudFront & JW Player](https://www.miracletutorials.com/hls-adaptive-streaming-tutorial-with-cloudfront-jw-player/)  - 
* [HOW TO: View an HLS Stream in QuickTime or VLC](https://softron.zendesk.com/hc/en-us/articles/207694617-HOW-TO-View-an-HLS-Stream-in-QuickTime-or-VLC?mobile_site=true)  - 
* [HTTP Live Streaming: HLS Player for Android | Toptal](https://www.toptal.com/apple/introduction-to-http-live-streaming-hls)  - 
* [How To Setup Nginx For HLS Video Streaming On Centos 7](https://dev.to/samuyi/how-to-setup-nginx-for-hls-video-streaming-on-centos-7-3jb8)  - 
* [How video streaming works on the web: An introduction](https://medium.com/canal-tech/how-video-streaming-works-on-the-web-an-introduction-7919739f7e1)  - 
* [Internet Video Streaming part 1](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-1-b10964849e19?source=userActivityShare-94bccb50d11-1559723768&_branch_match_id=664736558865703297)  - 
* [Internet Video Streaming? ABR part 2](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-2-dbce136b0d7c?source=userActivityShare-94bccb50d11-1559723862&_branch_match_id=664736952377004405)  - 
* [Live Playlist (Sliding Window) Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/live_playlist_sliding_window_construction)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part I](https://blog.twitch.tv/en/2017/10/10/live-video-transmuxing-transcoding-f-fmpeg-vs-twitch-transcoder-part-i-489c1c125f28/)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part II](https://blog.twitch.tv/live-video-transmuxing-transcoding-ffmpeg-vs-twitchtranscoder-part-ii-4973f475f8a3?source=userActivityShare-94bccb50d11-1561003748&_branch_match_id=670105191114382351&gi=fd8d504494f4)  - 
* [OTT Content Delivery](https://medium.com/@eyevinntechnology/ott-content-delivery-b43a35ef24f6)  - 
* [OTT Content Delivery Multi CDN](https://medium.com/@eyevinntechnology/ott-content-delivery-multi-cdn-8cd90ad2628a?source=userActivityShare-94bccb50d11-1560983307&_branch_match_id=670019455010399744)  - 
* [The structure of an MPEG-DASH MPD - Brendan Long](https://www.brendanlong.com/the-structure-of-an-mpeg-dash-mpd.html)  - 
* [Understanding the HTTP Live Streaming Architecture | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/understanding_the_http_live_streaming_architecture)  - 
* [Video Encoding Compression and Resolutions](https://medium.com/@eyevinntechnology/chessboard-for-beginners-video-encoding-compression-and-resolutions-bcefe04fa639)  - 
* [Video on Demand Playlist Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/video_on_demand_playlist_construction)  - 
* [bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X)](https://gist.github.com/mrbar42/ae111731906f958b396f30906004b3fa)  - 
* [create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS/)  - A tutorial to generate fMp4 files compatible with dash and HLS
* [digital_video_introduction: A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding).](https://github.com/leandromoreira/digital_video_introduction)  - A gentle introduction to video technology, although it's aimed at software developers / engineers, we want to make it easy for anyone to learn.
* [eyevinn/streaming-onboarding](https://github.com/Eyevinn/streaming-onboarding)  - 
* [ffmpeg audio/video manipulation](http://howto-pages.org/ffmpeg/)  - How to tame the Swiss army knife of audio and video manipulation
* [ffmpeg audio/video manipulation](http://howto-pages.org/ffmpeg/)  - 
* [matmoi/create-DASH-HLS: A tutorial to generate fMp4 files compatible with dash and HLS](https://github.com/matmoi/create-DASH-HLS)  - 

## HLS
*HLS tools, libraries, and resources.*

* [Advances in HTTP Live Streaming - WWDC 2017 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2017/504/)  - 
* [Advances in HTTP Live Streaming WWDC](https://devstreaming-cdn.apple.com/videos/wwdc/2017/504op4c3001w2f222/504/504_advances_in_http_live_streaming.pdf)  - 
* [AirPlay2 Example Code](https://developer.apple.com/documentation/avfoundation/airplay_2/integrating_airplay_for_long-form_video_apps)  - 
* [AirPlay2 WWDC 19 Slides](https://devstreaming-cdn.apple.com/videos/wwdc/2019/507fk9wyls0np6piwk/507/507_hls_authoring_for_airplay_2_video.pdf)  - 
* [Eyevinn/Hls-download](https://github.com/Eyevinn/hls-download)  - 
* [Eyevinn/hls-download](https://github.com/Eyevinn/hls-download)  - 
* [Eyevinn/hls-origin-scripts](https://github.com/Eyevinn/hls-origin-scripts)  - 
* [Eyevinn/hls-playlist-parser](https://github.com/Eyevinn/hls-playlist-parser)  - 
* [Eyevinn/hls-relay](https://github.com/Eyevinn/hls-relay)  - 
* [Eyevinn/hls-to-dash](https://github.com/Eyevinn/hls-to-dash)  - 
* [Eyevinn/hls-ts-analyzer](https://github.com/Eyevinn/hls-ts-analyzer)  - 
* [Eyevinn/hls-ts-js](https://github.com/Eyevinn/hls-ts-js)  - 
* [Eyevinn/manifestparser](https://github.com/Eyevinn/manifestparser)  - 
* [GitHub - Eyevinn/vod-to-live: A python library to generate Live HLS from VOD](https://github.com/Eyevinn/vod-to-live)  - 
* [HLS and Fragmented MP4 | HTTP Live Streaming](https://hlsbook.net/hls-fragmented-mp4/)  - At WWDC 2016, Apple announced support for fragmented MP4 (fMP4) as an alternative to MPEG-TS, which prior to their announcement was the only supported format.
* [HLS and Fragmented MP4 | HTTP Live Streaming](https://hlsbook.net/hls-fragmented-mp4/)  - 
* [HLS | Bento4](https://www.bento4.com/developers/hls/)  - 
* [HLSCore Swift HLS lib](https://github.com/fcanas/HLSCore)  - 
* [HLSDownloader](https://github.com/nmrony/hlsdownloader)  - Downloads m3u8 playlist and TS chunks for a given playlist URL.
* [HLSDownloader Swift](https://github.com/qi-shun-wang/HLSDownloader)  - 
* [HLSDownloader by nmrony](https://github.com/nmrony/hlsdownloader)  - 
* [Introducing Low-Latency HLS - WWDC 2019 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2019/502)  - 
* [Protocol Extension for Low-Latency HLS (Preliminary Specification) | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/protocol_extension_for_low-latency_hls_preliminary_specification#3291001)  - 
* [Validating HLS](https://devstreaming-cdn.apple.com/videos/wwdc/2016/510ndmh9wkcvzneegv2/510/510_validating_http_live_streams.pdf)  - 
* [auto-dash-hls](https://github.com/majamee/auto-dash-hls)  - 
* [denex/hls-downloader](https://github.com/denex/hls-downloader)  - 
* [hls-fetch](https://github.com/osklil/hls-fetch)  - 
* [hlsdl](https://github.com/selsta/hlsdl)  - 
* [iheartradio/open-m3u8: Open Source m3u8 Parser](https://github.com/iheartradio/open-m3u8)  - 
* [lcy0321/m3u8-downloader: Download the ts files according to the given m3u8 file.](https://github.com/lcy0321/m3u8-downloader)  - 
* [morsel Swift HLS library](https://github.com/krad/morsel)  - 
* [selsta/hlsdl: C program to download VoD HLS (.m3u8) files GitHub:](https://github.com/selsta/hlsdl)  - 
* [shrimpgo/video-downloader](https://github.com/shrimpgo/video-downloader)  - 
* [yuhuili-lab/Tide](https://github.com/yuhuili-lab/Tide)  - 

## DASH
*DASH tools, libraries, and resources.*

* [DASH-IF Conformance Software](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance)  - 
* [DASH-IF DASH Live Source Simulator](https://github.com/Dash-Industry-Forum/dash-live-source-simulator)  - 
* [DASH-IF Interoperability: Guidelines for Implementations](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf)  - 
* [DASH-IF Interoperability: Guidelines for Implementations](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf)  - 
* [Dash-Industry-Forum/dash.js](https://github.com/Dash-Industry-Forum/dash.js)  - 
* [Eyevinn/dash-validator-js](https://github.com/Eyevinn/dash-validator-js)  - 
* [Eyevinn/docker-2dash: A Docker container to pre-package MPEG DASH on demand content](https://github.com/Eyevinn/docker-2dash)  - 
* [Eyevinn/docker-dash-packager](https://github.com/Eyevinn/docker-dash-packager)  - 
* [Eyevinn/hls-to-dash](https://github.com/Eyevinn/hls-to-dash)  - 
* [Eyevinn/vp9-dash](https://github.com/Eyevinn/vp9-dash)  - 
* [ISO Segment Validator](https://github.com/Dash-Industry-Forum/ISOSegmentValidator)  - ISO BMFF, DASH, CMAF and HbbTV - DVB segment validation conformance
* [Viblast/dash-proxy](https://github.com/Viblast/dash-proxy)  - 
* [auto-dash-hls](https://github.com/majamee/auto-dash-hls)  - 
* [bitmovin/libdash](https://github.com/bitmovin/libdash)  - 
* [carlanton/mpd-tools](https://github.com/carlanton/mpd-tools)  - 
* [carlanton/mpd-tools: DASH MPD tools for Java](https://github.com/carlanton/mpd-tools)  - 
* [caststack/python-mpegdash](https://github.com/caststack/python-mpegdash)  - 
* [dash-proxy](https://github.com/Viblast/dash-proxy)  - Dash proxy is a tool that allows for easy downloading or mirroring of remote MPEG-DASH streams.
* [djvergad/dash](https://github.com/djvergad/dash)  - 
* [docker-dash-packager](https://github.com/Eyevinn/docker-dash-packager)  -  Docker container for an open source MPEG DASH packager
* [libdash](https://github.com/bitmovin/libdash)  - 
* [mahbubcseju/MPEG-DASH-Downloader](https://github.com/mahbubcseju/MPEG-DASH-Downloader)  - 
* [media-tools](https://github.com/Dash-Industry-Forum/media-tools)  - 
* [mp4dash | Bento4](https://www.bento4.com/documentation/mp4dash/)  - 
* [nickdesaulniers/combine-mpd](https://github.com/nickdesaulniers/combine-mpd)  - 
* [shengbinmeng/dash-drm](https://github.com/shengbinmeng/dash-drm)  - 
* [stultus/mp4-to-mpegdash-py](https://github.com/stultus/mp4-to-mpegdash-py)  - 
* [tchakabam/dash-proxy](https://github.com/tchakabam/dash-proxy)  - 
* [theolampert/dash-server](https://github.com/theolampert/dash-server)  - 
* [videojs/videojs-contrib-dash](https://github.com/videojs/videojs-contrib-dash)  - 

## Encoding
*Encoding tools, libraries, and resources.*

* [A Large-Scale Comparison of x264 x265 and libvpx](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f)  - Netflix Technology Blog.
* [A Large-Scale Comparison of x264 x265 and libvpx](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f)  - 
* [Bento4 | Fast, Modern Tools and C++ Class Library for all your MP4 and DASH media format needs](https://www.bento4.com/)  - 
* [Introducing SVT-AV1: a scalable open-source AV1 framework](https://medium.com/netflix-techblog/introducing-svt-av1-a-scalable-open-source-av1-framework-c726cce3103a)  - 
* [Video Transcoding API](https://github.com/video-dev/video-transcoding-api)  - 
* [bloc97/Anime4K](https://github.com/bloc97/Anime4K)  - 
* [cannonbeach/ott-packager](https://github.com/cannonbeach/ott-packager)  - 
* [demo-encoder](https://github.com/realeyes-media/demo-encoder/)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3
* [docker-bento4](https://github.com/alfg/docker-bento4)  - 
* [node-video-lib](https://github.com/gkozlenko/node-video-lib)  - 
* [nytimes/video-presets](https://github.com/nytimes/video-presets)  - 
* [olaris / olaris-server](https://gitlab.com/olaris/olaris-server)  - 
* [realeyes-media/alpine-node-video-multitool](https://github.com/realeyes-media/alpine-node-video-multitool)  - 
* [realeyes-media/demo-encoder: A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3](https://github.com/realeyes-media/demo-encoder)  - 

## Reading
*A list of reading articles, blogs, and newsletters for video streaming.*

* [9 Best Home Server Apps to Automate Media Management](https://www.smarthomebeginner.com/best-home-server-apps/)  - 
* [Battle of the Video Format: Comparing MKV vs MP4](https://bitmovin.com/mkv-vs-mp4/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz--KSAyThG9MNeSt28DH4ARDp3E1ujyIxyFCr2Dlctl7XcrajMAhRv2exdRRtgAFkaGnNIV_oDJgUAFV9joOCsDy-Vh_sw&_hsmi=80348170&utm_content=80347861&utm_source=hs_email&hsCtaTracking=a4ecf824-05b6-41b1-b600-20a1cd5b0cf6%7C1853ebeb-bdae-4e36-b131-2fdf6e65a93d)  - 
* [Extracting contextual information from video assets](https://medium.com/netflix-techblog/extracting-contextual-information-from-video-assets-ee9da25b6008)  - 
* [IMF: A Prescription for Versionitis](https://medium.com/netflix-techblog/imf-a-prescription-for-versionitis-e0b4c1865c20)  - 
* [Inside MPEG's Ambitious Plan to Launch 3 Video Codecs in 2020](https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Inside-MPEGs-Ambitious-Plan-to-Launch-3-Video-Codecs-in-2020-134694.aspx)  - 
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1559724204&_branch_match_id=664738392430917730)  - 
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1560983627&_branch_match_id=670020794794030328)  - 
* [Streaming Live From the Battlefield: Military Video in 2019](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=135141)  - 
* [The Netflix Content Processing Pipeline](https://medium.com/netflix-techblog/the-netflix-imf-workflow-f45dd72ed700?source=userActivityShare-94bccb50d11-1568773157&_branch_match_id=702692448596112473)  - 
* [Video in the War Zone: The Current State of Military Streaming](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=101310)  - 

## Specs & Standards
*Latest offical specs and standards related to video streaming.*

* [DASH-IF Interoperability: Guidelines for Implementations](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf)  - 
* [HLS Authoring Specification for Apple Devices](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - Describes the requirements for live and VOD audio-video content delivery using HTTP Live Streaming (HLS) to Apple devices.
* [HLS Authoring Specification for Apple Devices | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - 
* [HTTP Live Streaming 2nd Edition](https://tools.ietf.org/pdf/draft-pantos-hls-rfc8216bis-05.pdf)  - 
* [ISO - ISO/IEC 23009-1:2019 - Information technology -- Dynamic adaptive streaming over HTTP (DASH) -- Part 1: Media presentation description and segment formats](https://www.iso.org/standard/75485.html)  - 
* [SCTE Dash SPEC](https://www.scte.org/SCTEDocs/Standards/ANSI_SCTE%20214-1%202015.pdf)  - 
* [Standard audio A85-2013](https://www.atsc.org/wp-content/uploads/2015/03/Techniques-for-establishing-and-maintaining-audio-loudness.pdf)  - 

## Players
*Client players, libraries, tools, and examples.*

* [A curated list of awesome resources for building Smart TV apps](https://github.com/vitalets/awesome-smart-tv)  - 
* [Chromecast Receiver Docs](https://codelabs.developers.google.com/codelabs/cast-receiver/#0)  - 
* [Eyevinn/abr-player-chrome](https://github.com/Eyevinn/abr-player-chrome)  - 
* [Eyevinn/av1-player](https://github.com/Eyevinn/av1-player)  - 
* [Eyevinn/channel-engine-multiview](https://github.com/Eyevinn/channel-engine-multiview)  - 
* [Eyevinn/docker-html5player](https://github.com/Eyevinn/docker-html5player)  - 
* [Eyevinn/docker-html5player](https://github.com/Eyevinn/docker-html5player)  - 
* [Eyevinn/eyevinn-player](https://github.com/Eyevinn/eyevinn-player)  - 
* [Eyevinn/eyevinn-player](https://github.com/Eyevinn/eyevinn-player)  - 
* [Eyevinn/ott-multiview](https://github.com/Eyevinn/ott-multiview)  - 
* [MPEGDASHPlayer/MPEGDASH-iOS-Player](https://github.com/MPEGDASHPlayer/MPEGDASH-iOS-Player)  - 
* [Ruffle](https://github.com/ruffle-rs/ruffle)  - 
* [StyleShare/HLSCachingReverseProxyServer](https://github.com/StyleShare/HLSCachingReverseProxyServer)  - 
* [davidAgo4g/VideoPlayer-iOS: A library based on FFMPEG to play video files on iOS using OpenGLES and AudioQueue. Build with theos](https://github.com/davidAgo4g/VideoPlayer-iOS)  - 
* [googlecast/CastReceiver](https://github.com/googlecast/CastReceiver)  - 
* [imoreapps/ffmpeg-avplayer-for-ios-tvos: A tiny but powerful iOS and Apple TV OS av player framework that's based on the FFmpeg library.](https://github.com/imoreapps/ffmpeg-avplayer-for-ios-tvos)  - 
* [masterjk/ios-avplayer-http-capture: iOS based application that embeds the AVPlayer and capture HTTP headers and send it back to the iOS application. It internally embeds a proxy server.](https://github.com/masterjk/ios-avplayer-http-capture)  - 
* [peak3d/inputstream.adaptive](https://github.com/peak3d/inputstream.adaptive)  - 
* [tanersener/mobile-ffmpeg: FFmpeg for Android, iOS and tvOS](https://github.com/tanersener/mobile-ffmpeg)  - 
* [tjenkinson/media-element-syncer](https://github.com/tjenkinson/media-element-syncer)  - 
* [ustwo/videoplayback-ios](https://github.com/ustwo/videoplayback-ios)  - 

## FFMPEG
*FFMPEG libraries, configs, tools, and examples.*

* [ CRF Guide (Constant Rate Factor in x264, x265 and libvpx)](http://slhck.info/video/2017/02/24/crf-guide.html)  - The Constant Rate Factor (CRF) is the default quality (and rate control) setting for the x264 and x265 encoders 
* [CRF Guide (Constant Rate Factor in x264, x265 and libvpx)](http://slhck.info/video/2017/02/24/crf-guide.html)  - 
* [FFmpeg4Java 3.1.1-1.1](https://github.com/nextbreakpoint/ffmpeg4java)  - 
* [Generate MPEG-TS from file with ffmpeg](https://medium.com/@eyevinntechnology/generate-mpeg-ts-from-file-with-ffmpeg-7561181e6369?source=userActivityShare-94bccb50d11-1560983471&_branch_match_id=670020142756633081)  - 
* [How to generate a fmp4 hls live stream with FFMPEG](https://nomadyun.wordpress.com/2018/04/12/how-to-generate-a-fmp4-hls-live-stream-with-ffmpeg/)  - ffmpeg example command.
* [How to generate a fmp4 hls live stream with FFMPEG](https://nomadyun.wordpress.com/2018/04/12/how-to-generate-a-fmp4-hls-live-stream-with-ffmpeg/)  - 
* [Loop file and generate multiple video bitrates muxed in MPEG-TS with ffmpeg](https://medium.com/@eyevinntechnology/loop-file-and-generate-multiple-video-bitrates-muxed-in-mpeg-ts-with-ffmpeg-85658d0b74bb?source=userActivityShare-94bccb50d11-1560983383&_branch_match_id=670019768959110835)  - 
* [awesome-ffmpeg](ttps://github.com/transitive-bullshit/awesome-ffmpeg)  - A curated list of awesome FFmpeg resources.
* [compile and install latest ffmpeg source as pkg](https://gist.github.com/krzemienski/e51a0b7a6ba77e616f954e516783270c#file-compile-and-install-latest-ffmpeg-source-sh-L2)  - 
* [cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile master nvidia / container-images / samples GitLab](https://gitlab.com/nvidia/container-images/samples/blob/master/cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile)  - 
* [ffmpeg and hardware acceleration of HEVC transcoding](https://superuser.com/questions/1295957/ffmpeg-and-hardware-acceleration-of-hevc-transcoding-on-mac)  - ffmpeg -hide_banner -h encoder=hevc_videotoolbox 
* [ffmpeg audio/video manipulation](http://howto-pages.org/ffmpeg/)  - 
* [jrottenberg/ffmpeg: Docker build for FFmpeg on Ubuntu / Alpine / Centos 7 / Scratch](https://github.com/jrottenberg/ffmpeg)  - 
* [kokorin/Jaffree](https://github.com/kokorin/Jaffree)  - 
* [x264 FFmpeg Options Guide - Linux Encoding](https://sites.google.com/site/linuxencoding/x264-ffmpeg-mapping)  - 

## Audio
*Audio libraries, tools, and examples.*

* [ EBU R128 Introduction - Florian Camerer](https://www.youtube.com/watch?v=iuEtQqC-Sqo)  - 
* [Adjust and Normalize Your Music Files with FFMPEG - Make Tech Easier](https://www.maketecheasier.com/normalize-music-files-with-ffmpeg/)  - 
* [Audio Loudness Conversational Actions - Google Developers](https://developers.google.com/assistant/tools/audio-loudness)  - 
* [Audio normalization with ffmpeg using loudnorm (ebur128) filter? bytes and bones](https://bytesandbones.wordpress.com/2017/03/16/audio-nomalization-with-ffmpeg-using-loudnorm-ebur128-filter/)  - 
* [How To Normalize Audio - Why Do It? Everything You Need To Know](https://www.learndigitalaudio.com/normalize-audio)  - 
* [How to Set Audio Levels for Video](https://www.premiumbeat.com/blog/how-to-set-audio-levels-for-video/)  - 
* [Loudness Explained Page | Music Tribe - TC Electronic](https://www.tcelectronic.com/brand/tcelectronic/loudness-explained#googtrans(en|en))  - 
* [Multi Channel Audio codec evaluations](https://tech.ebu.ch/docs/tech/tech3324.pdf)  - 
* [Quick Tutorial: How to Increase Volume in Audacity [2019 Update]](https://www.iskysoft.com/video-editing/how-to-increase-volume-in-audacity.html)  - 
* [ReplayGain - Audacity Forum](https://forum.audacityteam.org/viewtopic.php?p=167758#p167758)  - 
* [Standard audio A85-2013](https://www.atsc.org/wp-content/uploads/2015/03/Techniques-for-establishing-and-maintaining-audio-loudness.pdf)  - 
* [hybrik-samples/ebu_r128_audio_normalization.json hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples/blob/master/Feature%20Examples/Filters/ebu_r128_audio_normalization.json)  - 
* [slhck/ffmpeg-normalize: Audio Normalization for Python/ffmpeg](https://github.com/slhck/ffmpeg-normalize#examples)  - 
* [superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform: Superpowered Audio, Networking and Cryptographics SDKs. High performance and cross platform on Android, iOS, macOS, tvOS, Linux, Windows and modern web browsers.](https://github.com/superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform)  - 

## Subtitles & Closed Captions
*Subtitling & Closed Caption libraries, tools, and examples.*

* [BingLingGroup/autosub: Command-line utility to transcribe/translate from video/audio/subtitles to subtitles](https://github.com/BingLingGroup/autosub)  - 
* [Can ffmpeg extract closed caption data - Stack Overflow](https://stackoverflow.com/questions/3169910/can-ffmpeg-extract-closed-caption-data)  - 
* [Caption Inspector](https://github.com/Comcast/caption-inspector)  - 
* [Closed Captions vs. Subtitles and why the Difference is Important - Matinee Multilingual](https://www.matinee.co.uk/blog/closed-captions-vs-subtitles-and-why-the-difference-is-important/)  - 
* [DVB-Sub Output Captions - MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html)  - 
* [Eyevinn/srt-metadata-extractor](https://github.com/Eyevinn/srt-metadata-extractor)  - 
* [Short-notes on Add subtitle to any video with ffmpeg](https://mahasak.com/short-notes-on-add-subtitle-to-any-video-with-ffmpeg/)  - 
* [Ultimate Guide to Closed Captioning](https://www.3playmedia.com/resources/popular-topics/closed-captioning/)  - 
* [Web Video Text Tracks Format (WebVTT) - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)  - 
* [abinashmeher999/voice-data-extract](https://github.com/abinashmeher999/voice-data-extract)  - 
* [active-video/subtitles](https://github.com/active-video/subtitles)  - 
* [alexherbo2/ffmpeg-sub](https://github.com/alexherbo2/ffmpeg-sub)  - 
* [apm1467/videocr](https://github.com/apm1467/videocr)  - 
* [awslabs/serverless-subtitles](https://github.com/awslabs/serverless-subtitles)  - 
* [cea608-extractor](https://github.com/Comcast/cea-extractor)  - 
* [cea608.js](https://github.com/Dash-Industry-Forum/cea608.js)  - 
* [cessen/subs_extract](https://github.com/cessen/subs_extract)  - 
* [federicocalendino/pysub-parser](https://github.com/federicocalendino/pysub-parser)  - 
* [jnorton001/pycaption-cli: A command line interface for the pycaption module.](https://github.com/jnorton001/pycaption-cli)  - 
* [pbs/pycaption: Python module to read/write popular video caption formats](https://github.com/pbs/pycaption)  - 
* [sarahs/caption_converter: Flask app based on https://github.com/pbs/pycaption](https://github.com/sarahs/caption_converter)  - 
* [shawnsky/extract-subtitles: Extract Subtitles From Video](https://github.com/shawnsky/extract-subtitles)  - 
* [statsbiblioteket/tv-subtitle-extraction](https://github.com/statsbiblioteket/tv-subtitle-extraction)  - 
* [xinnjie/extract-subtitle](https://github.com/xinnjie/extract-subtitle)  - 

## HEVC
*HEVC (h265) libraries, tools, examples, and resources.*

* [Apple Got It Wrong: Encoding Specs for HEVC in HLS](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=121878)  - Though I didn't recognize it at first, when Apple released its encoding specifications for HEVC and HLS, they got it wrong, though it took a comment from a true encoding expert to help me realize it.
* [Encoding Live and VOD for HEVC & HLS](https://streaminglearningcenter.com/wp-content/uploads/2018/05/Encoding-for-HEVC-SME-2018-Jan.pdf)  - 
* [Eyevinn/docker-hevc](https://github.com/Eyevinn/docker-hevc)  - 
* [Guide to HEVC/H.265 Encoding and Playback - TechSpot](https://www.techspot.com/article/1131-hevc-h256-enconding-playback/)  - 
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - 
* [HEVC Scientific overview](http://iphome.hhi.de/wiegand/assets/pdfs/2012_12_IEEE-HEVC-Overview.pdf)  - 
* [HEVC in HLS: 10 Key Questions for Streaming Video Developers](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=122637&PageNum=2)  - 
* [HEVC. Efficienty](https://ieeexplore.ieee.org/ielx7/76/7372356/07254155.pdf?tp=&arnumber=7254155&isnumber=7372356&ref=)  - 
* [HLS Authoring Update for HEVC](https://devstreaming-cdn.apple.com/videos/wwdc/2017/515vy4sl7iu70/515/515_hls_authoring_update.pdf)  - 
* [Jan Olzer on HLS HEVC](https://www.linkedin.com/pulse/market-significance-apples-adopting-hevc-heres-what-i-jan-ozer)  - 
* [Suggestion for x265's --tune film - Doom9's Forum](https://forum.doom9.org/showthread.php?t=172458)  - 
* [hevc video](https://youtu.be/p6dLZfs0jTY)  - 
* [hevc video part 1](https://youtu.be/TLNkK5C1KN8)  - 
* [hevc video part 2](https://youtu.be/V6a1AW5xyAw)  - 
* [multicoreware / x265 / wiki / Home](https://bitbucket.org/multicoreware/x265/wiki/Home)  - 
* [x265 Documentation ](https://x265.readthedocs.io/en/default/)  - 

## Ads
*Ads in streaming video related libraries, tools, examples, and resources.*

* [Eyevinn/adxchange-engine](https://github.com/Eyevinn/adxchange-engine)  - 
* [Eyevinn/vast-info](https://github.com/Eyevinn/vast-info)  - 
* [SCTE-104/35 and Beyond: A Look at Ad Insertion in an OTT World | TvTechnology](https://www.tvtechnology.com/opinions/scte10435-and-beyond-a-look-at-ad-insertion-in-an-ott-world)  - 
* [Understanding Server-Side Dynamic Ad Insertion - Eyevinn Technology - Medium](https://medium.com/@eyevinntechnology/understanding-server-side-dynamic-ad-insertion-d7ed90e34aa2)  - 

## Roku
*Roku app tools, libraries,and examples.*

* [Roku Developer | Documentation | Streaming specifications](https://developer.roku.com/docs/specs/streaming.md)  - 
* [XML + Code + Good times = RSG Application - Plex Labs - Medium](https://medium.com/plexlabs/xml-code-good-times-rsg-application-b963f0cec01b)  - 

## Dolby
*Dolby specs, libraries, examples, and tools.*

* [Dolby Vision for Content Creators | Dolby Laboratories](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creative-professionals.html)  - 
* [Dolby Vision streams within the HTTP Live Streaming format](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-streams-within-the-http-live-streaming-format-v2.0.pdf)  - 
* [DolbyProfessional Loudness](https://www.dolby.com/us/en/technologies/dolby-professional-loudness-solutions.pdf)  - 

## QoE & Analytics
*QoE & Analytics tools, libraries, and resources.*

* [JNoDuq/videobench: VMAF PSNR Bitrate Analyzer](https://github.com/JNoDuq/videobench)  - 
* [Netflix/vmaf](https://github.com/Netflix/vmaf/)  - 
* [Quality of Experience in Streaming](https://medium.com/@eyevinntechnology/quality-of-experience-in-streaming-5c25355a4111?source=userActivityShare-94bccb50d11-1559724940&_branch_match_id=664741478927428385)  - 
* [Toward A Practical Perceptual Video Quality Metric - Netflix TechBlog - Medium](https://medium.com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric-653f208b9652)  - 
* [VMAF: The Journey Continues - Netflix TechBlog - Medium](https://medium.com/netflix-techblog/vmaf-the-journey-continues-44b51ee9ed12)  - 
* [Video Bench - How to measure your video quality easily](https://medium.com/@jnoduq/video-bench-how-measure-your-video-quality-easily-85a0feb8f6e2)  - 
* [Video Quality Assessment](https://medium.com/@eyevinntechnology/video-quality-assessment-34abd35f96c0?source=userActivityShare-94bccb50d11-1560983815&_branch_match_id=670021582869771680)  - 
* [cta-wave/R4WG20-QoE-Metrics](https://github.com/cta-wave/R4WG20-QoE-Metrics)  - 

## Tools
*Streaming video tools and resources to make life easier.*

* [A Docker container with the video streaming tools you need](https://medium.com/@eyevinntechnology/a-docker-container-with-the-video-streaming-tools-you-need-b8319e98f36a)  - 
* [Aws video media convert docs](https://docs.aws.amazon.com/en_pv/mediaconvert/latest/ug/mediaconvert-guide.pdf#working-with-queues)  - 
* [Batch-Py-Remux](https://github.com/ZaifSenpai/Batch-Py-Remux)  - 
* [Bento4 | Fast, Modern Tools and C++ Class Library for all your MP4 and DASH media format needs](https://www.bento4.com/)  - 
* [Deep Video Analytics](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics)  - 
* [EEL - A simple Proxy Service for JSON Event Transformation and Forwarding](https://github.com/Comcast/eel)  - 
* [Eyevinn/docker-jit-capture](https://github.com/Eyevinn/docker-jit-capture)  - 
* [Eyevinn/docker-serve: A simple Python based HTTP server that sets CORS allow headers. Useful for streaming from files on local computer](https://github.com/Eyevinn/docker-serve)  - 
* [Eyevinn/fmp4-js](https://github.com/Eyevinn/fmp4-js)  - 
* [Eyevinn/pseudo-live-playout](https://github.com/Eyevinn/pseudo-live-playout)  - 
* [Eyevinn/streaming-analyzer](https://github.com/Eyevinn/streaming-analyzer)  - 
* [Eyevinn/toolbox: A set of Docker containers with Streaming tools](https://github.com/Eyevinn/toolbox)  - 
* [Eyevinn/vod-to-live.js](https://github.com/Eyevinn/vod-to-live.js)  - 
* [Go library for mpeg ts](https://github.com/Comcast/gots)  - 
* [Gpac](https://github.com/gpac/gpac)  - 
* [IMF Conversion Utility](https://github.com/DSRCorporation/imf-conversion)  - 
* [Inca - Netflix](https://link.medium.com/Lu3GnIPeg0)  - 
* [Mamba](https://github.com/Comcast/mamba)  - 
* [Marcos-A/STRCleaner](https://github.com/Marcos-A/STRCleaner)  - 
* [Open Broadcaster Software | OBS](https://obsproject.com/)  - 
* [alpine-bento-ffmpeg](https://github.com/realeyes-media/alpine-bento-ffmpeg)  - 
* [channel-engine](https://github.com/Eyevinn/channel-engine)  - 
* [coopernurse/nginx-s3-proxy](https://github.com/coopernurse/nginx-s3-proxy)  - 
* [estliberitas/node-thumbnails-webvtt: Video thumbnail generator generating WebVTT spec file](https://github.com/estliberitas/node-thumbnails-webvtt)  - 
* [jkarthic-akamai/ABR-Broadcaster: A real time encoder for Adaptive Bitrate Broadcast](https://github.com/jkarthic-akamai/ABR-Broadcaster)  - 
* [liwf616/awesome-live-stream](https://github.com/liwf616/awesome-live-stream)  - 
* [mar10/wsgidav: A generic and extendable WebDAV server based on WSGI](https://github.com/mar10/wsgidav)  - 
* [minio/minio: MinIO is a high performance object storage server compatible with Amazon S3 APIs](https://github.com/minio/minio)  - 
* [node-video-lib](https://github.com/gkozlenko/node-video-lib)  - 
* [nytimes/video-presets](https://github.com/nytimes/video-presets)  - 
* [obsproject/obs-studio: OBS Studio - Free and open source software for live streaming and screen recording](https://github.com/obsproject/obs-studio)  - 
* [realeyes-media/alpine-node-video-multitool](https://github.com/realeyes-media/alpine-node-video-multitool)  - 
* [scte35-js](https://github.com/Comcast/scte35-js)  - 
* [video-on-demand-on-aws.pdf](https://s3.amazonaws.com/solutions-reference/video-on-demand-on-aws/latest/video-on-demand-on-aws.pdf)  - 
* [watson-developer-cloud/text-to-speech-nodejs](https://github.com/watson-developer-cloud/text-to-speech-nodejs)  - 

## DRM
*DRM tools, documentations, and resources.*

* [Content Protection for HLS with AES-128 Encryption](https://www.theoplayer.com/blog/content-protection-for-hls-with-aes-128-encryption)  - 
* [CrackerCat/video_decrypter](https://github.com/CrackerCat/video_decrypter)  - 
* [Digital Rights Management (DRM) - Everything you need to know](https://bitmovin.com/digital-rights-management-everything-to-know/)  - 
* [Encryption & DRM with Multiple Keys? Unified Streaming](https://docs.unified-streaming.com/documentation/package/multiple-keys.html)  - 
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - Since time eternal, the streaming industry has toiled with and extolled the virtues of CODECs and their key enablement of the entire digital video experience.
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - 
* [HLS Key Specs](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-00#section-5.1)  - HLS Key Files
* [HLS Key Specs](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-00#section-5.1)  - 
* [Secure Apple HLS streaming using DRM encryption](https://www.wowza.com/docs/how-to-secure-apple-hls-streaming-using-drm-encryption)  - 
* [Securing OTT Content - DRM](https://medium.com/@eyevinntechnology/securing-ott-content-drm-1af2c08fdd31?source=userActivityShare-94bccb50d11-1560983518&_branch_match_id=670020366479331042)  - 
* [aes-decrypter](https://github.com/videojs/aes-decrypter)  - 
* [shengbinmeng/dash-drm](https://github.com/shengbinmeng/dash-drm)  - 

## Testing
*Video streaming testing tools and helpers.*

* [17 Free MPEG-DASH example and HLS m3u8 sample test streams](https://bitmovin.com/mpeg-dash-hls-examples-sample-streams/)  - Collection of publicly available and free MPEG-DASH and HLS examples, test streams and datasets to help you through your development process
* [4K Media | Free Ultra-HD / HDR / HLG / Dolby Vision 4K Video Demos & Samples](https://4kmedia.org/)  - Sample 4K HDR HLG AND Dolby Vision content
* [Automated testing on devices - Netflix TechBlog - Medium](http://techblog.netflix.com/2016/08/automated-testing-on-devices.html)  - 
* [HLS Test Suite From Eurofins Digital Testing - Free HLS Test Streams and Test Cases](https://hlstests.eurofins-digitaltesting.com/)  - 
* [HTTP Live Streaming (HLS) - Artillery.io Docs](https://artillery.io/docs/plugin-hls/)  - 
* [Xiph.org Test Media](https://media.xiph.org/)  - 
* [artilleryio/artillery-plugin-hls](https://github.com/artilleryio/artillery-plugin-hls)  - 
* [bengarney/list-of-streams](https://github.com/bengarney/list-of-streams)  - 

## Talks & Presentations
*Conference talks and presentations on streaming video .*

* [Advances in HTTP Live Streaming - WWDC 2017](https://developer.apple.com/videos/play/wwdc2017/504/)  - Videos - Apple Developer
* [Advances in HTTP Live Streaming - WWDC 2017 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2017/504/)  - 
* [Video Insiders Podcast](https://thevideoinsiders.simplecast.com/episodes)  - 
* [mhv/2019 Talks](http://mile-high.video/files/mhv2019/)  - 

## Books
*Books on video streaming.*

* [Communicating Pictures - 1st Edition](https://www.elsevier.com/books/communicating-pictures/bull/978-0-12-405906-1)  - 

## CDN
*Last mile tools, documentations, and resources.*

* [Amazon S3 as Origin Fastly tutorial](https://docs.fastly.com/guides/integrations/amazon-s3#using-amazon-s3-as-an-origin)  - 
* [Delivering Live Streaming Video with CloudFront and AWS Media Services - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)  - 
* [Delivering Live Streaming Video with CloudFront and AWS Media Services - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)  - 
* [Edge Computing with Fastly CDN and Varnish VCL for Authenticated Requests](https://endertech.com/blog/edge-computing-fastly-cdn-varnish-vcl-authenticated-requests)  - 
* [Fastly compared to Amazon CloudFront](https://www.cdnoverview.com/compare/fastly-vs-amazon-cloudfront/)  - 
* [How to use DASH and HLS Adaptive Streaming with AWS S3 and Cloudfront](https://bitmovin.zendesk.com/hc/en-us/articles/115001609634-How-to-use-DASH-and-HLS-Adaptive-Streaming-with-AWS-S3-and-Cloudfront)  - 
* [Lambda@Edge Design Best Practices | Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/)  - 
* [OTT Content Delivery CDN Alternatives](https://medium.com/@eyevinntechnology/ott-content-delivery-cdn-alternatives-cafe75dab71d?source=userActivityShare-94bccb50d11-1560983135&_branch_match_id=670018733519578135)  - 
* [On-Demand and Live Streaming Video with CloudFront - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html)  - 
* [Optimizing High Availability with CloudFront Origin Failover - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html)  - 
* [Tutorial: Creating a Simple Lambda@Edge Function - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html)  - 


### Contributing

Please take a quick look at the [contribution guidelines](.github/CONTRIBUTING.md) first. If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you to all [contributors](https://github.com/matteocrippa/awesome-swift/graphs/contributors); you rock!!