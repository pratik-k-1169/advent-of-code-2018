#!/usr/bin/env python3
f = """[1518-04-11 00:44] wakes up
[1518-08-26 00:21] wakes up
[1518-11-11 00:12] falls asleep
[1518-09-05 00:59] wakes up
[1518-03-22 00:09] wakes up
[1518-03-19 00:41] wakes up
[1518-04-15 00:10] falls asleep
[1518-02-06 23:52] Guard #3109 begins shift
[1518-11-04 00:43] falls asleep
[1518-09-12 00:51] wakes up
[1518-11-18 00:31] falls asleep
[1518-02-09 00:25] falls asleep
[1518-04-15 00:17] wakes up
[1518-04-22 00:16] falls asleep
[1518-11-03 00:02] Guard #2459 begins shift
[1518-03-11 00:42] falls asleep
[1518-07-07 23:58] Guard #3109 begins shift
[1518-06-25 23:48] Guard #1327 begins shift
[1518-09-05 00:55] falls asleep
[1518-04-24 00:09] falls asleep
[1518-03-12 00:59] wakes up
[1518-03-19 00:04] Guard #239 begins shift
[1518-10-05 23:59] Guard #2459 begins shift
[1518-04-16 00:46] falls asleep
[1518-10-31 00:46] wakes up
[1518-10-14 00:02] Guard #2459 begins shift
[1518-09-21 23:59] Guard #2999 begins shift
[1518-03-17 00:59] wakes up
[1518-07-04 23:47] Guard #1069 begins shift
[1518-03-11 00:55] wakes up
[1518-08-22 00:36] wakes up
[1518-07-09 00:52] wakes up
[1518-02-24 00:25] falls asleep
[1518-05-26 00:58] wakes up
[1518-11-23 00:38] falls asleep
[1518-05-17 00:14] falls asleep
[1518-04-13 00:47] falls asleep
[1518-03-24 00:51] wakes up
[1518-05-01 00:27] falls asleep
[1518-07-05 00:12] wakes up
[1518-05-19 00:40] falls asleep
[1518-04-28 00:29] falls asleep
[1518-03-12 00:27] wakes up
[1518-05-11 00:00] Guard #2411 begins shift
[1518-11-01 00:00] Guard #1327 begins shift
[1518-10-06 00:27] falls asleep
[1518-08-05 00:53] wakes up
[1518-03-07 23:46] Guard #2999 begins shift
[1518-06-16 00:32] falls asleep
[1518-02-25 00:37] falls asleep
[1518-11-09 00:36] falls asleep
[1518-08-12 00:21] wakes up
[1518-07-14 00:22] falls asleep
[1518-09-25 00:34] wakes up
[1518-04-17 00:01] Guard #2003 begins shift
[1518-11-21 00:35] falls asleep
[1518-07-31 00:42] wakes up
[1518-03-26 23:59] Guard #2411 begins shift
[1518-02-08 00:02] falls asleep
[1518-05-31 00:42] wakes up
[1518-09-04 00:21] falls asleep
[1518-11-09 00:57] falls asleep
[1518-07-16 00:01] Guard #2459 begins shift
[1518-02-15 00:00] Guard #811 begins shift
[1518-07-03 00:42] wakes up
[1518-05-07 00:03] Guard #239 begins shift
[1518-07-21 23:50] Guard #2411 begins shift
[1518-02-07 00:30] wakes up
[1518-05-13 23:56] Guard #1291 begins shift
[1518-06-10 00:46] wakes up
[1518-07-09 23:47] Guard #1069 begins shift
[1518-09-21 00:22] falls asleep
[1518-02-21 00:50] falls asleep
[1518-08-22 00:58] wakes up
[1518-03-02 00:48] wakes up
[1518-07-23 00:54] wakes up
[1518-06-15 00:59] wakes up
[1518-09-19 00:28] falls asleep
[1518-04-18 00:55] wakes up
[1518-09-08 00:50] wakes up
[1518-06-12 00:00] Guard #2381 begins shift
[1518-08-06 00:06] wakes up
[1518-10-04 00:03] Guard #1381 begins shift
[1518-02-06 00:03] Guard #2411 begins shift
[1518-10-01 00:58] wakes up
[1518-06-26 00:41] wakes up
[1518-04-16 00:03] Guard #191 begins shift
[1518-07-29 00:26] falls asleep
[1518-08-01 23:58] Guard #2999 begins shift
[1518-05-01 00:55] wakes up
[1518-05-28 00:12] falls asleep
[1518-06-18 00:52] wakes up
[1518-03-13 23:59] Guard #1009 begins shift
[1518-10-12 00:56] wakes up
[1518-04-27 00:05] falls asleep
[1518-07-18 00:57] falls asleep
[1518-08-28 00:29] falls asleep
[1518-09-12 23:56] Guard #1381 begins shift
[1518-11-01 00:48] wakes up
[1518-11-11 00:38] falls asleep
[1518-06-18 23:50] Guard #1229 begins shift
[1518-07-01 00:32] wakes up
[1518-04-16 00:41] wakes up
[1518-03-26 00:54] falls asleep
[1518-02-10 00:55] wakes up
[1518-09-11 00:33] falls asleep
[1518-03-08 00:25] falls asleep
[1518-08-06 00:04] falls asleep
[1518-07-31 00:01] falls asleep
[1518-02-13 00:37] falls asleep
[1518-08-08 00:28] falls asleep
[1518-02-18 23:59] Guard #2459 begins shift
[1518-04-25 00:01] Guard #1381 begins shift
[1518-03-25 00:12] falls asleep
[1518-10-13 00:44] wakes up
[1518-05-03 00:35] falls asleep
[1518-08-21 00:35] falls asleep
[1518-07-09 00:43] falls asleep
[1518-05-02 00:13] falls asleep
[1518-10-12 00:32] falls asleep
[1518-02-17 00:33] falls asleep
[1518-09-04 00:50] falls asleep
[1518-11-08 00:57] wakes up
[1518-05-20 23:57] Guard #941 begins shift
[1518-03-23 00:57] wakes up
[1518-04-21 00:09] falls asleep
[1518-03-18 00:03] Guard #2381 begins shift
[1518-04-10 00:12] wakes up
[1518-11-17 00:19] falls asleep
[1518-10-06 00:24] wakes up
[1518-07-13 00:01] Guard #2411 begins shift
[1518-06-20 23:57] Guard #283 begins shift
[1518-07-13 23:59] Guard #1229 begins shift
[1518-06-12 00:28] wakes up
[1518-10-30 00:08] wakes up
[1518-11-06 00:28] falls asleep
[1518-02-21 00:00] Guard #941 begins shift
[1518-11-19 00:47] wakes up
[1518-07-18 00:58] wakes up
[1518-10-04 00:11] falls asleep
[1518-08-16 00:28] falls asleep
[1518-05-19 00:21] falls asleep
[1518-03-10 00:59] wakes up
[1518-07-12 00:10] falls asleep
[1518-02-22 00:00] Guard #941 begins shift
[1518-10-02 00:56] falls asleep
[1518-10-03 00:51] wakes up
[1518-06-29 00:39] wakes up
[1518-07-07 00:27] wakes up
[1518-09-16 00:09] falls asleep
[1518-07-22 00:40] wakes up
[1518-11-11 00:45] wakes up
[1518-09-11 23:56] Guard #191 begins shift
[1518-07-13 00:35] falls asleep
[1518-10-27 00:00] Guard #2053 begins shift
[1518-10-05 00:32] wakes up
[1518-08-15 00:45] wakes up
[1518-09-28 00:46] wakes up
[1518-06-05 00:01] Guard #811 begins shift
[1518-11-23 00:00] Guard #1229 begins shift
[1518-11-09 00:53] wakes up
[1518-02-08 00:16] wakes up
[1518-11-21 00:46] wakes up
[1518-07-30 00:48] wakes up
[1518-10-08 00:49] wakes up
[1518-06-11 00:06] falls asleep
[1518-06-13 00:51] falls asleep
[1518-10-29 00:29] falls asleep
[1518-10-15 00:00] Guard #1327 begins shift
[1518-08-18 00:03] falls asleep
[1518-05-09 00:27] wakes up
[1518-05-27 00:08] falls asleep
[1518-02-15 00:31] wakes up
[1518-10-13 00:42] falls asleep
[1518-08-10 00:04] falls asleep
[1518-03-05 00:03] Guard #2137 begins shift
[1518-03-08 00:03] falls asleep
[1518-11-14 00:27] wakes up
[1518-03-12 00:47] falls asleep
[1518-07-21 00:54] wakes up
[1518-07-21 00:01] Guard #191 begins shift
[1518-08-26 00:58] wakes up
[1518-04-26 23:47] Guard #2003 begins shift
[1518-11-10 23:59] Guard #811 begins shift
[1518-03-07 00:35] wakes up
[1518-11-14 00:22] falls asleep
[1518-09-25 00:02] Guard #2999 begins shift
[1518-06-07 00:03] Guard #3109 begins shift
[1518-09-20 00:13] wakes up
[1518-11-04 00:51] wakes up
[1518-03-21 00:48] falls asleep
[1518-08-29 00:01] Guard #2003 begins shift
[1518-06-07 23:56] Guard #1069 begins shift
[1518-04-29 00:46] wakes up
[1518-10-27 23:57] Guard #137 begins shift
[1518-06-28 00:00] Guard #941 begins shift
[1518-04-06 00:44] falls asleep
[1518-11-03 00:59] wakes up
[1518-08-21 00:47] wakes up
[1518-07-20 00:37] falls asleep
[1518-03-13 00:26] wakes up
[1518-03-27 00:49] wakes up
[1518-06-05 00:31] wakes up
[1518-11-19 00:00] falls asleep
[1518-07-01 00:11] falls asleep
[1518-11-23 00:56] falls asleep
[1518-11-07 00:47] falls asleep
[1518-11-05 00:56] wakes up
[1518-06-22 00:51] wakes up
[1518-06-27 00:21] falls asleep
[1518-03-15 00:00] Guard #1327 begins shift
[1518-08-27 00:56] wakes up
[1518-08-28 00:24] wakes up
[1518-06-07 00:44] wakes up
[1518-07-10 00:17] wakes up
[1518-08-28 00:47] wakes up
[1518-05-18 00:09] falls asleep
[1518-04-04 00:37] falls asleep
[1518-02-22 00:48] wakes up
[1518-02-10 00:19] falls asleep
[1518-03-01 00:35] falls asleep
[1518-05-19 00:00] Guard #2003 begins shift
[1518-09-14 00:50] wakes up
[1518-02-05 00:58] wakes up
[1518-11-23 00:49] wakes up
[1518-06-19 00:07] wakes up
[1518-10-02 00:02] falls asleep
[1518-07-16 00:55] wakes up
[1518-05-05 00:29] wakes up
[1518-11-22 00:53] wakes up
[1518-05-14 23:49] Guard #1009 begins shift
[1518-08-20 00:03] Guard #1009 begins shift
[1518-04-05 23:58] Guard #811 begins shift
[1518-05-08 00:04] Guard #1069 begins shift
[1518-09-01 00:04] Guard #1229 begins shift
[1518-02-17 00:42] wakes up
[1518-05-04 00:53] falls asleep
[1518-07-21 00:22] falls asleep
[1518-09-18 23:58] Guard #3109 begins shift
[1518-03-09 00:34] falls asleep
[1518-07-08 23:58] Guard #239 begins shift
[1518-05-14 00:41] wakes up
[1518-08-13 23:59] Guard #2459 begins shift
[1518-08-30 23:51] Guard #239 begins shift
[1518-03-23 00:16] wakes up
[1518-11-18 23:52] Guard #3109 begins shift
[1518-07-03 00:11] falls asleep
[1518-10-18 00:19] falls asleep
[1518-06-29 00:57] wakes up
[1518-11-22 00:43] falls asleep
[1518-05-03 00:47] wakes up
[1518-11-09 00:02] Guard #1291 begins shift
[1518-05-16 00:48] falls asleep
[1518-08-24 00:11] falls asleep
[1518-03-26 00:11] wakes up
[1518-02-13 00:57] wakes up
[1518-10-15 00:36] falls asleep
[1518-06-26 00:03] falls asleep
[1518-06-11 00:01] Guard #941 begins shift
[1518-06-03 00:03] Guard #239 begins shift
[1518-06-08 00:54] wakes up
[1518-05-25 00:29] wakes up
[1518-11-01 00:31] falls asleep
[1518-08-02 00:23] falls asleep
[1518-11-08 00:31] wakes up
[1518-09-11 00:46] falls asleep
[1518-10-19 00:37] falls asleep
[1518-09-20 00:41] falls asleep
[1518-06-25 00:18] wakes up
[1518-06-19 00:37] wakes up
[1518-11-03 00:18] falls asleep
[1518-02-26 00:03] Guard #239 begins shift
[1518-10-21 00:24] falls asleep
[1518-05-28 00:04] Guard #2411 begins shift
[1518-03-07 00:40] falls asleep
[1518-06-10 00:01] falls asleep
[1518-08-23 00:51] wakes up
[1518-11-20 00:00] Guard #1069 begins shift
[1518-07-24 00:06] falls asleep
[1518-07-22 00:12] falls asleep
[1518-05-27 00:30] wakes up
[1518-10-06 23:58] Guard #3463 begins shift
[1518-03-26 00:45] falls asleep
[1518-07-25 23:47] Guard #1229 begins shift
[1518-03-14 00:54] falls asleep
[1518-04-05 00:45] wakes up
[1518-04-04 00:51] wakes up
[1518-08-01 00:32] falls asleep
[1518-08-22 00:55] falls asleep
[1518-03-09 23:56] Guard #2381 begins shift
[1518-11-14 00:38] wakes up
[1518-09-11 00:20] falls asleep
[1518-08-29 00:32] wakes up
[1518-02-20 00:02] Guard #2381 begins shift
[1518-10-24 00:14] falls asleep
[1518-06-22 00:21] falls asleep
[1518-07-30 00:56] wakes up
[1518-06-22 23:46] Guard #2411 begins shift
[1518-06-01 23:59] Guard #239 begins shift
[1518-04-01 00:58] wakes up
[1518-02-25 00:47] wakes up
[1518-05-24 00:03] Guard #3109 begins shift
[1518-07-30 23:51] Guard #191 begins shift
[1518-10-23 00:34] wakes up
[1518-05-08 23:58] Guard #2999 begins shift
[1518-07-15 00:22] falls asleep
[1518-02-07 00:48] wakes up
[1518-06-19 00:03] falls asleep
[1518-02-28 00:59] wakes up
[1518-07-21 00:27] wakes up
[1518-04-25 23:57] Guard #2411 begins shift
[1518-06-15 00:12] falls asleep
[1518-05-08 00:14] wakes up
[1518-06-27 00:56] falls asleep
[1518-09-16 23:56] Guard #2137 begins shift
[1518-11-22 00:32] wakes up
[1518-09-28 00:21] falls asleep
[1518-03-22 00:27] wakes up
[1518-10-29 00:51] wakes up
[1518-05-23 00:25] falls asleep
[1518-02-26 00:55] wakes up
[1518-06-08 23:58] Guard #1381 begins shift
[1518-02-24 00:57] falls asleep
[1518-06-18 00:17] falls asleep
[1518-06-20 00:43] falls asleep
[1518-05-13 00:04] Guard #137 begins shift
[1518-09-03 00:02] Guard #3109 begins shift
[1518-02-16 00:19] falls asleep
[1518-07-10 00:21] falls asleep
[1518-03-09 00:49] wakes up
[1518-02-05 00:54] wakes up
[1518-05-09 00:32] wakes up
[1518-05-02 23:53] Guard #191 begins shift
[1518-08-22 00:00] Guard #1069 begins shift
[1518-04-02 00:38] wakes up
[1518-07-23 00:09] falls asleep
[1518-10-11 00:54] wakes up
[1518-04-12 00:00] Guard #2137 begins shift
[1518-09-13 00:17] falls asleep
[1518-04-26 00:57] wakes up
[1518-08-07 00:57] falls asleep
[1518-09-09 00:59] wakes up
[1518-07-06 00:42] wakes up
[1518-07-08 00:41] wakes up
[1518-02-24 00:43] wakes up
[1518-02-07 00:03] falls asleep
[1518-06-07 00:27] falls asleep
[1518-04-17 23:52] Guard #2459 begins shift
[1518-09-23 00:01] Guard #2897 begins shift
[1518-03-23 00:50] falls asleep
[1518-05-08 00:12] falls asleep
[1518-06-24 00:09] falls asleep
[1518-03-18 00:57] wakes up
[1518-11-02 00:24] wakes up
[1518-07-05 23:51] Guard #1009 begins shift
[1518-08-13 00:14] falls asleep
[1518-07-24 00:35] falls asleep
[1518-10-26 00:00] Guard #2381 begins shift
[1518-08-12 00:41] falls asleep
[1518-09-25 00:08] falls asleep
[1518-03-10 00:40] wakes up
[1518-08-07 00:53] wakes up
[1518-06-27 00:59] wakes up
[1518-11-06 23:56] Guard #2053 begins shift
[1518-03-30 00:31] falls asleep
[1518-11-06 00:57] falls asleep
[1518-04-06 00:49] wakes up
[1518-08-02 00:53] falls asleep
[1518-06-09 23:50] Guard #1229 begins shift
[1518-07-18 23:57] Guard #1229 begins shift
[1518-07-03 00:01] Guard #2381 begins shift
[1518-04-19 00:52] wakes up
[1518-06-06 00:04] Guard #941 begins shift
[1518-03-23 23:59] Guard #2897 begins shift
[1518-02-23 00:02] Guard #941 begins shift
[1518-08-02 00:56] wakes up
[1518-04-15 00:42] falls asleep
[1518-08-23 00:17] falls asleep
[1518-07-08 00:47] falls asleep
[1518-06-17 00:03] Guard #811 begins shift
[1518-03-12 00:04] falls asleep
[1518-07-07 00:09] falls asleep
[1518-03-25 23:51] Guard #3109 begins shift
[1518-08-23 23:56] Guard #941 begins shift
[1518-06-13 23:49] Guard #3109 begins shift
[1518-10-24 00:02] Guard #2459 begins shift
[1518-09-05 00:51] wakes up
[1518-02-28 00:50] falls asleep
[1518-05-25 00:26] falls asleep
[1518-07-08 00:27] falls asleep
[1518-08-14 00:53] falls asleep
[1518-10-17 00:36] wakes up
[1518-08-30 00:45] falls asleep
[1518-09-25 00:11] wakes up
[1518-06-19 23:58] Guard #2459 begins shift
[1518-03-22 00:04] Guard #811 begins shift
[1518-05-21 00:54] wakes up
[1518-08-03 00:58] wakes up
[1518-04-24 00:46] wakes up
[1518-06-01 00:53] wakes up
[1518-04-05 00:00] Guard #2003 begins shift
[1518-07-23 00:00] Guard #2003 begins shift
[1518-02-09 00:11] wakes up
[1518-09-21 00:06] falls asleep
[1518-06-29 23:57] Guard #2003 begins shift
[1518-11-22 00:39] wakes up
[1518-08-14 00:47] wakes up
[1518-10-06 00:41] falls asleep
[1518-05-15 23:58] Guard #1009 begins shift
[1518-11-13 00:44] wakes up
[1518-02-17 00:02] Guard #941 begins shift
[1518-10-04 00:53] wakes up
[1518-11-11 23:57] Guard #191 begins shift
[1518-10-27 00:21] falls asleep
[1518-08-08 00:56] wakes up
[1518-11-05 00:35] falls asleep
[1518-08-19 00:34] wakes up
[1518-11-07 00:43] wakes up
[1518-03-03 00:34] wakes up
[1518-11-15 00:57] wakes up
[1518-10-01 23:52] Guard #1069 begins shift
[1518-08-28 00:43] wakes up
[1518-10-30 00:06] falls asleep
[1518-08-10 00:59] wakes up
[1518-03-13 00:13] wakes up
[1518-09-11 00:35] wakes up
[1518-08-21 00:57] falls asleep
[1518-02-16 00:00] Guard #239 begins shift
[1518-04-16 00:55] wakes up
[1518-06-06 00:54] wakes up
[1518-03-19 00:15] falls asleep
[1518-09-25 00:22] falls asleep
[1518-09-16 00:42] falls asleep
[1518-05-23 00:59] wakes up
[1518-05-30 00:01] Guard #1229 begins shift
[1518-06-24 00:54] wakes up
[1518-07-11 00:56] wakes up
[1518-03-15 23:57] Guard #239 begins shift
[1518-10-19 00:59] wakes up
[1518-08-14 00:54] wakes up
[1518-03-03 00:54] wakes up
[1518-10-17 00:30] falls asleep
[1518-02-08 23:52] Guard #191 begins shift
[1518-07-18 00:00] Guard #1327 begins shift
[1518-04-16 00:29] wakes up
[1518-08-20 00:55] wakes up
[1518-06-26 00:46] falls asleep
[1518-05-04 00:49] wakes up
[1518-09-13 00:30] falls asleep
[1518-05-15 00:01] falls asleep
[1518-02-06 00:43] wakes up
[1518-08-14 00:39] wakes up
[1518-08-25 00:44] wakes up
[1518-05-12 00:26] wakes up
[1518-05-09 00:22] falls asleep
[1518-10-02 00:46] wakes up
[1518-09-04 00:43] wakes up
[1518-07-28 00:18] falls asleep
[1518-03-08 00:59] wakes up
[1518-04-02 00:03] falls asleep
[1518-08-16 00:20] falls asleep
[1518-09-02 00:39] falls asleep
[1518-06-17 00:32] falls asleep
[1518-11-07 00:54] wakes up
[1518-11-14 00:59] wakes up
[1518-04-28 23:57] Guard #2999 begins shift
[1518-06-25 00:16] falls asleep
[1518-07-30 00:02] Guard #811 begins shift
[1518-07-31 23:56] Guard #2999 begins shift
[1518-04-25 00:53] falls asleep
[1518-10-30 00:18] falls asleep
[1518-05-17 00:00] Guard #2999 begins shift
[1518-05-20 00:53] wakes up
[1518-08-21 00:04] wakes up
[1518-06-27 00:00] Guard #2053 begins shift
[1518-02-16 00:57] wakes up
[1518-10-16 00:40] falls asleep
[1518-09-11 00:58] wakes up
[1518-10-20 00:16] falls asleep
[1518-04-30 23:59] Guard #1229 begins shift
[1518-07-24 00:30] wakes up
[1518-03-14 00:58] wakes up
[1518-07-29 00:49] wakes up
[1518-04-16 00:28] falls asleep
[1518-05-26 00:21] falls asleep
[1518-02-11 00:06] falls asleep
[1518-05-10 00:19] falls asleep
[1518-08-24 00:19] wakes up
[1518-08-17 00:16] falls asleep
[1518-05-24 00:49] falls asleep
[1518-03-27 00:35] wakes up
[1518-09-16 00:55] wakes up
[1518-11-16 00:03] falls asleep
[1518-06-13 00:34] falls asleep
[1518-11-22 00:22] falls asleep
[1518-04-23 00:00] Guard #3109 begins shift
[1518-04-12 00:53] wakes up
[1518-04-11 00:03] Guard #1069 begins shift
[1518-08-01 00:23] falls asleep
[1518-09-20 00:47] wakes up
[1518-10-12 00:01] Guard #1009 begins shift
[1518-09-22 00:21] falls asleep
[1518-03-04 00:54] wakes up
[1518-04-17 00:55] wakes up
[1518-10-21 00:46] wakes up
[1518-03-23 00:02] Guard #811 begins shift
[1518-09-19 00:56] wakes up
[1518-03-14 00:41] wakes up
[1518-09-10 00:54] wakes up
[1518-08-28 00:20] falls asleep
[1518-06-20 00:37] wakes up
[1518-06-26 00:30] wakes up
[1518-06-29 00:04] Guard #1381 begins shift
[1518-08-28 00:46] falls asleep
[1518-07-01 23:58] Guard #1229 begins shift
[1518-02-25 00:57] falls asleep
[1518-10-20 23:59] Guard #1009 begins shift
[1518-03-01 00:48] wakes up
[1518-09-27 00:34] wakes up
[1518-02-11 00:00] Guard #1291 begins shift
[1518-08-01 00:36] wakes up
[1518-08-22 00:11] falls asleep
[1518-08-25 00:01] falls asleep
[1518-02-05 00:57] falls asleep
[1518-10-14 00:11] falls asleep
[1518-07-29 00:52] falls asleep
[1518-02-05 00:50] falls asleep
[1518-02-12 00:54] wakes up
[1518-07-25 00:01] Guard #2999 begins shift
[1518-10-06 00:21] falls asleep
[1518-11-07 00:13] falls asleep
[1518-04-23 00:32] wakes up
[1518-05-31 00:40] falls asleep
[1518-10-03 00:00] Guard #2003 begins shift
[1518-05-18 00:54] wakes up
[1518-08-27 00:00] Guard #1381 begins shift
[1518-05-25 23:59] Guard #2053 begins shift
[1518-11-09 00:59] wakes up
[1518-05-19 00:22] wakes up
[1518-05-22 00:04] Guard #3109 begins shift
[1518-08-11 00:02] Guard #137 begins shift
[1518-03-06 23:52] Guard #1291 begins shift
[1518-03-21 00:19] falls asleep
[1518-10-05 00:00] Guard #2411 begins shift
[1518-10-28 23:58] Guard #3463 begins shift
[1518-08-04 00:04] Guard #239 begins shift
[1518-05-04 00:58] wakes up
[1518-02-17 00:59] wakes up
[1518-05-04 00:00] Guard #2003 begins shift
[1518-10-02 00:59] wakes up
[1518-07-17 00:45] wakes up
[1518-02-13 00:04] Guard #2053 begins shift
[1518-04-20 00:58] wakes up
[1518-05-11 00:23] falls asleep
[1518-08-18 00:21] wakes up
[1518-09-29 00:51] falls asleep
[1518-05-05 00:24] falls asleep
[1518-03-06 00:53] wakes up
[1518-09-02 00:57] wakes up
[1518-08-23 00:04] Guard #2411 begins shift
[1518-10-22 00:20] falls asleep
[1518-07-24 00:51] falls asleep
[1518-09-29 00:53] wakes up
[1518-11-17 00:03] Guard #2003 begins shift
[1518-05-28 00:33] wakes up
[1518-04-25 00:57] falls asleep
[1518-08-20 23:54] Guard #239 begins shift
[1518-03-07 00:01] falls asleep
[1518-05-12 00:00] Guard #2999 begins shift
[1518-08-09 23:52] Guard #2411 begins shift
[1518-06-04 00:18] falls asleep
[1518-07-06 00:03] falls asleep
[1518-09-29 00:14] falls asleep
[1518-07-27 23:59] Guard #239 begins shift
[1518-04-23 00:49] wakes up
[1518-04-07 00:26] wakes up
[1518-09-26 00:36] falls asleep
[1518-08-04 23:59] Guard #941 begins shift
[1518-09-08 00:43] falls asleep
[1518-09-21 00:19] wakes up
[1518-07-30 00:39] falls asleep
[1518-09-26 00:00] Guard #239 begins shift
[1518-08-20 00:53] falls asleep
[1518-06-19 00:19] falls asleep
[1518-04-14 00:00] Guard #3463 begins shift
[1518-06-02 00:53] wakes up
[1518-02-17 00:53] falls asleep
[1518-10-26 00:08] falls asleep
[1518-06-06 00:25] falls asleep
[1518-11-12 23:58] Guard #1291 begins shift
[1518-04-24 00:02] Guard #3109 begins shift
[1518-03-23 00:15] falls asleep
[1518-02-18 00:52] falls asleep
[1518-04-21 00:43] falls asleep
[1518-09-27 00:08] falls asleep
[1518-06-11 00:08] wakes up
[1518-08-26 00:36] falls asleep
[1518-02-22 00:31] falls asleep
[1518-03-06 00:02] Guard #1327 begins shift
[1518-11-10 00:27] falls asleep
[1518-07-12 00:45] falls asleep
[1518-03-21 00:37] wakes up
[1518-04-20 00:55] falls asleep
[1518-07-22 00:57] wakes up
[1518-06-24 00:40] falls asleep
[1518-03-17 00:04] Guard #811 begins shift
[1518-02-06 00:07] falls asleep
[1518-02-15 00:49] falls asleep
[1518-10-10 00:37] wakes up
[1518-10-29 23:57] Guard #2999 begins shift
[1518-03-07 00:51] wakes up
[1518-07-22 00:35] falls asleep
[1518-07-30 00:36] wakes up
[1518-06-03 23:59] Guard #3109 begins shift
[1518-11-17 00:26] wakes up
[1518-02-26 00:43] wakes up
[1518-11-06 00:29] wakes up
[1518-06-24 00:03] Guard #191 begins shift
[1518-09-27 23:59] Guard #2999 begins shift
[1518-04-21 00:03] Guard #2137 begins shift
[1518-07-14 00:52] wakes up
[1518-09-07 00:33] falls asleep
[1518-11-12 00:37] wakes up
[1518-04-03 00:59] wakes up
[1518-06-06 00:52] falls asleep
[1518-10-25 00:47] wakes up
[1518-04-26 00:12] falls asleep
[1518-10-06 00:36] wakes up
[1518-02-26 00:34] falls asleep
[1518-10-08 00:45] falls asleep
[1518-09-21 00:39] wakes up
[1518-04-19 00:24] falls asleep
[1518-09-14 00:26] falls asleep
[1518-05-05 23:47] Guard #2137 begins shift
[1518-11-14 23:58] Guard #811 begins shift
[1518-10-03 00:08] falls asleep
[1518-04-04 00:21] wakes up
[1518-04-08 00:52] wakes up
[1518-02-12 00:00] Guard #2999 begins shift
[1518-09-03 00:56] wakes up
[1518-11-06 00:59] wakes up
[1518-06-08 00:26] falls asleep
[1518-09-04 00:57] wakes up
[1518-03-15 00:49] wakes up
[1518-07-16 00:37] falls asleep
[1518-08-16 00:57] wakes up
[1518-07-12 00:27] wakes up
[1518-02-19 00:30] falls asleep
[1518-05-01 23:58] Guard #2999 begins shift
[1518-02-07 23:50] Guard #2411 begins shift
[1518-10-16 00:59] wakes up
[1518-10-27 00:48] wakes up
[1518-04-23 00:38] falls asleep
[1518-02-20 00:11] falls asleep
[1518-07-24 00:48] wakes up
[1518-04-04 00:18] falls asleep
[1518-09-01 00:39] falls asleep
[1518-02-19 00:46] wakes up
[1518-03-08 00:22] wakes up
[1518-04-23 00:19] falls asleep
[1518-03-19 00:48] falls asleep
[1518-11-06 00:44] wakes up
[1518-11-06 00:00] Guard #2003 begins shift
[1518-06-16 00:00] Guard #2459 begins shift
[1518-10-11 00:42] falls asleep
[1518-07-05 00:02] falls asleep
[1518-08-21 00:03] falls asleep
[1518-03-11 23:49] Guard #1327 begins shift
[1518-06-09 00:46] wakes up
[1518-10-25 00:22] falls asleep
[1518-06-26 00:40] falls asleep
[1518-11-09 00:48] falls asleep
[1518-08-10 00:37] wakes up
[1518-03-07 00:28] falls asleep
[1518-02-23 00:07] falls asleep
[1518-09-23 23:53] Guard #2411 begins shift
[1518-11-11 00:31] wakes up
[1518-03-28 00:29] falls asleep
[1518-07-02 00:09] falls asleep
[1518-04-28 00:14] falls asleep
[1518-11-08 00:34] falls asleep
[1518-04-05 00:13] falls asleep
[1518-03-04 00:03] Guard #191 begins shift
[1518-06-27 00:48] wakes up
[1518-03-07 00:58] wakes up
[1518-08-05 00:42] falls asleep
[1518-03-20 00:53] wakes up
[1518-08-14 00:19] falls asleep
[1518-05-16 00:17] falls asleep
[1518-03-22 00:19] falls asleep
[1518-05-18 00:44] wakes up
[1518-06-26 00:47] wakes up
[1518-03-05 00:31] wakes up
[1518-09-27 00:01] Guard #2137 begins shift
[1518-06-24 00:37] wakes up
[1518-05-06 00:19] wakes up
[1518-09-09 23:57] Guard #1381 begins shift
[1518-06-01 00:00] Guard #1009 begins shift
[1518-03-14 00:09] falls asleep
[1518-02-20 00:35] wakes up
[1518-04-18 00:04] falls asleep
[1518-02-09 00:53] wakes up
[1518-09-06 00:38] wakes up
[1518-08-17 00:43] wakes up
[1518-08-14 23:57] Guard #1291 begins shift
[1518-03-21 00:00] Guard #1381 begins shift
[1518-08-04 00:23] falls asleep
[1518-04-22 00:54] wakes up
[1518-05-09 00:57] wakes up
[1518-11-14 00:46] falls asleep
[1518-03-07 00:54] falls asleep
[1518-06-09 00:49] falls asleep
[1518-08-13 00:25] wakes up
[1518-05-03 00:01] falls asleep
[1518-05-07 00:36] falls asleep
[1518-11-08 00:42] wakes up
[1518-05-19 00:47] wakes up
[1518-10-10 23:58] Guard #1229 begins shift
[1518-03-24 00:29] falls asleep
[1518-04-21 00:51] wakes up
[1518-10-12 00:33] wakes up
[1518-07-24 00:59] wakes up
[1518-11-09 00:44] wakes up
[1518-09-09 00:56] falls asleep
[1518-04-12 00:13] falls asleep
[1518-07-30 00:51] falls asleep
[1518-05-28 00:49] wakes up
[1518-10-12 23:59] Guard #239 begins shift
[1518-05-24 00:41] wakes up
[1518-10-09 00:26] wakes up
[1518-05-20 00:11] falls asleep
[1518-03-02 23:57] Guard #1229 begins shift
[1518-09-03 23:57] Guard #2897 begins shift
[1518-09-20 00:02] Guard #2381 begins shift
[1518-05-24 00:55] wakes up
[1518-10-19 00:00] Guard #2897 begins shift
[1518-03-07 00:25] wakes up
[1518-10-09 00:59] wakes up
[1518-11-12 00:06] falls asleep
[1518-10-13 00:48] falls asleep
[1518-02-23 23:59] Guard #1229 begins shift
[1518-04-16 00:37] falls asleep
[1518-03-15 00:31] falls asleep
[1518-08-26 00:09] falls asleep
[1518-07-05 00:56] wakes up
[1518-05-10 00:00] Guard #2897 begins shift
[1518-09-13 00:27] wakes up
[1518-04-08 00:24] falls asleep
[1518-05-28 23:59] Guard #1069 begins shift
[1518-03-28 00:54] wakes up
[1518-05-12 00:21] falls asleep
[1518-11-02 00:00] Guard #2137 begins shift
[1518-08-12 00:48] wakes up
[1518-02-05 00:00] Guard #3109 begins shift
[1518-07-11 00:55] falls asleep
[1518-06-11 00:42] wakes up
[1518-10-25 00:00] Guard #1069 begins shift
[1518-02-12 00:29] wakes up
[1518-08-18 23:59] Guard #2897 begins shift
[1518-03-13 00:08] falls asleep
[1518-03-21 00:53] wakes up
[1518-09-12 00:17] falls asleep
[1518-05-29 00:58] wakes up
[1518-06-06 00:07] falls asleep
[1518-03-31 00:20] falls asleep
[1518-06-02 00:44] falls asleep
[1518-05-09 00:30] falls asleep
[1518-10-12 00:55] falls asleep
[1518-11-09 23:59] Guard #2003 begins shift
[1518-04-27 23:58] Guard #1381 begins shift
[1518-05-12 00:49] falls asleep
[1518-07-21 00:48] falls asleep
[1518-08-02 23:56] Guard #941 begins shift
[1518-05-29 00:27] falls asleep
[1518-10-01 00:46] falls asleep
[1518-03-02 00:17] falls asleep
[1518-05-15 00:54] wakes up
[1518-07-12 00:01] Guard #1009 begins shift
[1518-09-18 00:38] falls asleep
[1518-09-04 23:59] Guard #2411 begins shift
[1518-06-20 00:57] wakes up
[1518-03-10 00:33] falls asleep
[1518-06-12 00:13] falls asleep
[1518-11-20 00:29] falls asleep
[1518-08-21 00:23] wakes up
[1518-11-22 00:01] Guard #2137 begins shift
[1518-08-31 00:57] wakes up
[1518-07-27 00:40] falls asleep
[1518-06-29 00:09] falls asleep
[1518-10-07 00:49] falls asleep
[1518-05-24 23:57] Guard #2999 begins shift
[1518-08-14 00:45] falls asleep
[1518-03-29 00:29] falls asleep
[1518-08-30 00:56] wakes up
[1518-10-15 23:56] Guard #1009 begins shift
[1518-05-01 00:06] falls asleep
[1518-09-10 00:25] falls asleep
[1518-09-13 00:41] wakes up
[1518-02-27 23:56] Guard #811 begins shift
[1518-11-04 00:03] Guard #3463 begins shift
[1518-07-22 00:56] falls asleep
[1518-10-18 00:34] wakes up
[1518-06-25 00:55] wakes up
[1518-09-03 00:54] falls asleep
[1518-08-12 23:57] Guard #191 begins shift
[1518-09-27 00:42] falls asleep
[1518-04-30 00:45] wakes up
[1518-11-03 00:46] wakes up
[1518-04-07 23:56] Guard #2999 begins shift
[1518-04-01 00:49] falls asleep
[1518-08-08 00:49] falls asleep
[1518-10-10 00:00] Guard #1291 begins shift
[1518-03-02 00:35] falls asleep
[1518-04-13 00:51] wakes up
[1518-10-18 00:00] Guard #2003 begins shift
[1518-04-01 00:35] wakes up
[1518-09-13 23:56] Guard #1291 begins shift
[1518-06-28 00:52] wakes up
[1518-06-27 00:47] falls asleep
[1518-07-30 00:16] falls asleep
[1518-05-01 00:14] wakes up
[1518-08-31 00:02] falls asleep
[1518-03-16 00:19] falls asleep
[1518-05-28 00:41] falls asleep
[1518-10-17 00:39] falls asleep
[1518-07-03 23:59] Guard #191 begins shift
[1518-06-03 00:52] falls asleep
[1518-04-28 00:36] wakes up
[1518-04-29 00:13] falls asleep
[1518-02-18 00:59] wakes up
[1518-09-16 00:00] Guard #1381 begins shift
[1518-06-21 23:56] Guard #191 begins shift
[1518-09-06 23:57] Guard #941 begins shift
[1518-08-08 00:34] wakes up
[1518-11-16 00:30] wakes up
[1518-02-07 00:41] falls asleep
[1518-06-29 00:44] falls asleep
[1518-10-05 00:10] falls asleep
[1518-07-15 00:36] wakes up
[1518-10-31 00:21] falls asleep
[1518-06-23 00:49] wakes up
[1518-06-14 00:50] wakes up
[1518-03-01 23:57] Guard #1009 begins shift
[1518-06-06 00:43] wakes up
[1518-09-29 00:43] wakes up
[1518-07-25 00:20] falls asleep
[1518-09-06 00:18] falls asleep
[1518-09-21 00:03] Guard #191 begins shift
[1518-10-20 00:26] wakes up
[1518-08-24 23:50] Guard #1381 begins shift
[1518-04-07 00:04] Guard #2999 begins shift
[1518-07-24 00:02] Guard #191 begins shift
[1518-03-09 00:03] Guard #2053 begins shift
[1518-03-25 00:57] wakes up
[1518-05-23 00:04] Guard #1291 begins shift
[1518-05-18 00:02] Guard #1291 begins shift
[1518-09-24 00:57] wakes up
[1518-07-12 00:57] wakes up
[1518-03-16 00:39] wakes up
[1518-08-29 23:56] Guard #1381 begins shift
[1518-09-23 00:40] wakes up
[1518-04-01 00:29] falls asleep
[1518-10-08 00:00] Guard #1381 begins shift
[1518-06-14 00:04] falls asleep
[1518-04-17 00:16] falls asleep
[1518-02-28 23:56] Guard #1229 begins shift
[1518-10-22 23:50] Guard #239 begins shift
[1518-05-04 00:13] falls asleep
[1518-11-14 00:03] Guard #1291 begins shift
[1518-08-21 00:59] wakes up
[1518-09-18 00:03] Guard #2411 begins shift
[1518-07-27 00:07] falls asleep
[1518-09-01 00:56] wakes up
[1518-07-01 00:00] Guard #2999 begins shift
[1518-02-26 23:56] Guard #2897 begins shift
[1518-11-10 00:46] wakes up
[1518-06-04 00:36] wakes up
[1518-03-18 00:48] falls asleep
[1518-04-10 00:07] falls asleep
[1518-06-16 00:59] wakes up
[1518-09-18 00:58] wakes up
[1518-10-17 00:58] wakes up
[1518-03-27 23:56] Guard #1381 begins shift
[1518-10-06 00:42] wakes up
[1518-09-07 00:56] wakes up
[1518-02-24 00:59] wakes up
[1518-05-27 00:00] Guard #2003 begins shift
[1518-06-28 00:29] falls asleep
[1518-09-30 00:00] Guard #137 begins shift
[1518-02-11 00:44] wakes up
[1518-07-20 00:00] Guard #3463 begins shift
[1518-05-10 00:21] wakes up
[1518-08-11 23:58] Guard #1009 begins shift
[1518-04-30 00:39] falls asleep
[1518-06-18 00:02] Guard #1229 begins shift
[1518-06-02 00:57] falls asleep
[1518-09-23 00:46] wakes up
[1518-03-16 00:50] wakes up
[1518-10-09 00:00] Guard #3109 begins shift
[1518-08-07 00:58] wakes up
[1518-03-31 00:59] wakes up
[1518-10-10 00:59] wakes up
[1518-11-18 00:00] Guard #2411 begins shift
[1518-04-14 00:49] wakes up
[1518-02-15 00:59] wakes up
[1518-11-15 23:51] Guard #1069 begins shift
[1518-08-10 00:42] falls asleep
[1518-04-14 23:56] Guard #2411 begins shift
[1518-03-27 00:27] falls asleep
[1518-07-20 00:52] wakes up
[1518-10-15 00:56] wakes up
[1518-02-13 23:58] Guard #137 begins shift
[1518-08-12 00:08] falls asleep
[1518-07-17 00:42] falls asleep
[1518-08-01 00:25] wakes up
[1518-03-31 23:57] Guard #239 begins shift
[1518-03-20 00:04] Guard #1291 begins shift
[1518-08-17 23:48] Guard #1069 begins shift
[1518-08-27 00:16] falls asleep
[1518-06-27 00:41] wakes up
[1518-09-26 00:58] wakes up
[1518-05-17 00:47] wakes up
[1518-10-16 23:57] Guard #191 begins shift
[1518-07-10 00:28] wakes up
[1518-04-19 00:01] Guard #1327 begins shift
[1518-02-09 23:57] Guard #2411 begins shift
[1518-05-16 00:35] wakes up
[1518-10-13 00:58] wakes up
[1518-05-14 00:09] falls asleep
[1518-07-04 00:21] wakes up
[1518-07-22 00:04] wakes up
[1518-10-09 00:36] falls asleep
[1518-10-22 00:44] wakes up
[1518-08-19 00:32] falls asleep
[1518-03-19 00:49] wakes up
[1518-06-20 00:15] falls asleep
[1518-03-30 00:46] wakes up
[1518-03-17 00:06] falls asleep
[1518-07-29 00:56] wakes up
[1518-03-16 00:42] falls asleep
[1518-11-08 00:56] falls asleep
[1518-08-17 00:04] Guard #239 begins shift
[1518-03-11 00:00] Guard #1009 begins shift
[1518-03-26 00:02] falls asleep
[1518-03-26 00:58] wakes up
[1518-08-18 00:35] falls asleep
[1518-11-22 00:36] falls asleep
[1518-05-17 00:18] falls asleep
[1518-11-03 00:55] falls asleep
[1518-09-23 00:37] falls asleep
[1518-05-22 00:12] falls asleep
[1518-07-25 00:50] wakes up
[1518-07-27 00:46] wakes up
[1518-06-14 23:59] Guard #3109 begins shift
[1518-02-17 23:56] Guard #1327 begins shift
[1518-05-14 00:38] falls asleep
[1518-05-19 00:11] falls asleep
[1518-03-02 00:28] wakes up
[1518-03-29 00:51] wakes up
[1518-07-06 23:56] Guard #2999 begins shift
[1518-08-15 00:21] falls asleep
[1518-08-29 00:20] falls asleep
[1518-09-11 00:23] wakes up
[1518-02-23 00:43] wakes up
[1518-07-15 00:03] Guard #191 begins shift
[1518-08-16 00:25] wakes up
[1518-04-30 00:00] Guard #1069 begins shift
[1518-09-08 00:04] Guard #3109 begins shift
[1518-06-05 00:28] falls asleep
[1518-07-17 00:00] Guard #1291 begins shift
[1518-10-22 00:03] Guard #1291 begins shift
[1518-10-01 00:01] Guard #239 begins shift
[1518-06-02 00:58] wakes up
[1518-05-19 00:15] wakes up
[1518-08-16 00:00] Guard #2999 begins shift
[1518-05-30 00:34] wakes up
[1518-09-06 00:03] Guard #1229 begins shift
[1518-07-22 00:02] falls asleep
[1518-07-26 23:56] Guard #1381 begins shift
[1518-09-20 00:09] falls asleep
[1518-11-06 00:36] falls asleep
[1518-02-09 00:05] falls asleep
[1518-03-06 00:24] falls asleep
[1518-11-07 23:59] Guard #1327 begins shift
[1518-11-08 00:18] falls asleep
[1518-05-02 00:32] wakes up
[1518-04-02 23:56] Guard #2459 begins shift
[1518-09-17 00:21] wakes up
[1518-03-30 00:02] Guard #1327 begins shift
[1518-04-25 00:54] wakes up
[1518-05-31 00:02] Guard #1381 begins shift
[1518-07-02 00:47] wakes up
[1518-05-24 00:37] falls asleep
[1518-11-14 00:30] falls asleep
[1518-08-04 00:57] wakes up
[1518-09-24 00:05] falls asleep
[1518-08-03 00:06] falls asleep
[1518-03-12 00:51] wakes up
[1518-03-13 00:04] Guard #1229 begins shift
[1518-07-05 00:17] falls asleep
[1518-06-09 00:24] falls asleep
[1518-09-14 23:58] Guard #137 begins shift
[1518-05-16 00:57] wakes up
[1518-02-12 00:48] falls asleep
[1518-11-18 00:45] wakes up
[1518-09-17 00:11] falls asleep
[1518-08-05 23:52] Guard #2137 begins shift
[1518-09-16 00:23] wakes up
[1518-09-11 00:02] Guard #2003 begins shift
[1518-08-21 00:21] falls asleep
[1518-08-02 00:28] wakes up
[1518-05-12 00:57] wakes up
[1518-02-21 00:57] wakes up
[1518-04-28 00:16] wakes up
[1518-09-23 00:45] falls asleep
[1518-05-30 00:14] falls asleep
[1518-04-21 23:59] Guard #941 begins shift
[1518-11-15 00:49] falls asleep
[1518-05-03 00:30] wakes up
[1518-04-04 00:02] Guard #1291 begins shift
[1518-02-27 00:54] wakes up
[1518-06-03 00:59] wakes up
[1518-05-18 00:49] falls asleep
[1518-09-09 00:00] Guard #811 begins shift
[1518-05-22 00:46] wakes up
[1518-06-09 00:56] wakes up
[1518-09-22 00:30] wakes up
[1518-08-28 00:00] Guard #2003 begins shift
[1518-06-01 00:18] falls asleep
[1518-03-03 00:39] falls asleep
[1518-03-24 23:58] Guard #2381 begins shift
[1518-06-25 00:03] Guard #2459 begins shift
[1518-09-03 00:46] falls asleep
[1518-11-13 00:30] falls asleep
[1518-07-28 00:30] wakes up
[1518-08-09 00:02] Guard #2003 begins shift
[1518-04-14 00:37] falls asleep
[1518-04-13 00:03] Guard #3463 begins shift
[1518-07-13 00:42] wakes up
[1518-03-04 00:20] falls asleep
[1518-09-05 00:49] falls asleep
[1518-03-22 00:08] falls asleep
[1518-03-12 00:56] falls asleep
[1518-06-23 00:01] falls asleep
[1518-02-12 00:24] falls asleep
[1518-07-28 23:57] Guard #3463 begins shift
[1518-04-28 00:52] wakes up
[1518-07-04 00:13] falls asleep
[1518-04-11 00:33] falls asleep
[1518-03-13 00:21] falls asleep
[1518-02-26 00:47] falls asleep
[1518-11-05 00:00] Guard #1229 begins shift
[1518-05-20 00:03] Guard #1009 begins shift
[1518-08-07 00:02] Guard #2381 begins shift
[1518-07-10 00:39] falls asleep
[1518-10-30 00:55] wakes up
[1518-04-03 00:35] falls asleep
[1518-02-25 00:58] wakes up
[1518-07-19 00:35] falls asleep
[1518-10-23 00:03] falls asleep
[1518-06-13 00:00] Guard #1069 begins shift
[1518-06-13 00:46] wakes up
[1518-05-14 00:23] wakes up
[1518-06-17 00:57] wakes up
[1518-11-20 00:47] wakes up
[1518-05-17 00:15] wakes up
[1518-05-11 00:57] wakes up
[1518-04-15 00:58] wakes up
[1518-05-07 00:47] wakes up
[1518-06-30 00:25] falls asleep
[1518-11-20 23:59] Guard #2053 begins shift
[1518-03-30 23:58] Guard #3109 begins shift
[1518-03-20 00:37] falls asleep
[1518-04-21 00:22] wakes up
[1518-05-05 00:00] Guard #1327 begins shift
[1518-10-09 00:20] falls asleep
[1518-08-07 00:14] falls asleep
[1518-10-14 00:55] wakes up
[1518-10-10 00:15] falls asleep
[1518-07-22 00:31] wakes up
[1518-05-06 00:00] falls asleep
[1518-06-13 00:52] wakes up
[1518-08-08 00:01] Guard #3463 begins shift
[1518-08-09 00:09] falls asleep
[1518-04-20 00:01] Guard #1009 begins shift
[1518-06-06 00:20] wakes up
[1518-07-19 00:58] wakes up
[1518-06-30 00:50] wakes up
[1518-03-26 00:49] wakes up
[1518-04-28 00:42] falls asleep
[1518-09-27 00:49] wakes up
[1518-03-29 00:00] Guard #1069 begins shift
[1518-10-20 00:04] Guard #2137 begins shift
[1518-10-26 00:46] wakes up
[1518-09-29 00:00] Guard #2411 begins shift
[1518-04-27 00:33] wakes up
[1518-07-27 00:19] wakes up
[1518-11-23 00:59] wakes up
[1518-02-27 00:37] falls asleep
[1518-07-08 00:55] wakes up
[1518-08-09 00:58] wakes up
[1518-03-10 00:52] falls asleep
[1518-10-24 00:56] wakes up
[1518-10-07 00:52] wakes up
[1518-02-25 00:01] Guard #1229 begins shift
[1518-05-21 00:32] falls asleep
[1518-07-26 00:05] falls asleep
[1518-04-07 00:10] falls asleep
[1518-08-26 00:00] Guard #2459 begins shift
[1518-10-10 00:43] falls asleep
[1518-03-05 00:12] falls asleep
[1518-05-09 00:56] falls asleep
[1518-04-01 23:48] Guard #2897 begins shift
[1518-10-31 00:02] Guard #3463 begins shift
[1518-07-10 00:55] wakes up
[1518-03-27 00:40] falls asleep
[1518-02-15 00:19] falls asleep
[1518-06-11 00:28] falls asleep
[1518-09-02 00:00] Guard #1229 begins shift
[1518-03-03 00:26] falls asleep
[1518-04-09 23:59] Guard #1381 begins shift
[1518-05-22 00:43] falls asleep
[1518-07-26 00:32] wakes up
[1518-06-25 00:42] falls asleep
[1518-09-03 00:51] wakes up
[1518-04-08 00:07] falls asleep
[1518-05-22 00:25] wakes up
[1518-11-02 00:06] falls asleep
[1518-04-09 00:03] Guard #283 begins shift
[1518-04-25 00:58] wakes up
[1518-07-10 00:03] falls asleep
[1518-07-11 00:03] Guard #2459 begins shift
[1518-08-18 00:55] wakes up
[1518-04-08 00:18] wakes up"""
import collections
import copy
import operator

def find_guard():
    events = f.split("\n")
    events_dict={}
    sleep_schedule = {}
    for event in events:
        events_dict[event[1:event.index(']')]] = event[event.index(']')+1:]
    od = collections.OrderedDict(sorted(events_dict.items()))

    for key,value in od.items():
        if 'Guard' in value:
            id = key+" -> "+value.split(" ")[2]
            sleep_schedule[id] = []
        elif 'falls' in value:
            sleep_schedule[id].append(int(key[-2:]))
        elif 'wakes' in value:
            sleep_schedule[id].append(int(key[-2:]))

    sleeps = copy.deepcopy(sleep_schedule)
    for guard_id,pattern in sleeps.items():
        total_sleep = 0
        for index,number in enumerate(pattern):
            if index % 2 == 0:
                total_sleep = total_sleep - int(number)
            else:
                total_sleep = total_sleep + int(number)
        sleeps[guard_id] = total_sleep

    total_sleeps = {}
    for key,value in sleeps.items():
        total_sleeps[key.split(' ')[-1]] = total_sleeps.get(key.split(' ')[-1],0) + value

    # for key,value in total_sleeps.items():
    #     print(key,value)

    max_sleep = max(total_sleeps.values())

    for guard_id,time in total_sleeps.items():
        if time == max_sleep:
            actual_id = guard_id

    # print(f"GUARD_ID: {actual_id}")

    patterns = []
    for guard_id,time in sleep_schedule.items():
        if guard_id.endswith(actual_id):
            patterns.append(time)

    full_patterns = []

    for each_pattern in patterns:
        complete = []
        for i in range(0,len(each_pattern),2):
            complete = complete + list(range(each_pattern[i],each_pattern[i+1]))
        full_patterns.append(complete)

    common_minute = {}
    for each_pattern in full_patterns:
        for minute in each_pattern:
            common_minute[str(minute)] = common_minute.get(str(minute),0) + 1

    sorted_minute = sorted(common_minute.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_minute[0])

find_guard()

