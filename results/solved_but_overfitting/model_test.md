## Hyper parameters used:
	batch_size=512
	buffer_size=1048576
	discount=0.995
	episodes=1000
	eval=False
	exploration_noise=0.1
	load_model_path=''
	lr_actor=0.001
	lr_critic=0.001
	max_timesteps=1000
	noise_clip=0.5
	policy_noise=0.2
	result_folder='C:\\Fevre\\Code\\Python\\TD3_continues_control\\results'
	seed=0
	slow_and_pretty=False
	steps_before_train=20
	tau=0.01
	train_delay=2
	train_iterations=10
	weight_decay=1e-06
##Training stats:
	Episode 1	Average Score: 0.84 	 current mean: 0.84	 Min:0.00	Max:2.30	Duration:17.95
	Episode 2	Average Score: 0.86 	 current mean: 0.88	 Min:0.14	Max:1.79	Duration:15.63
	Episode 3	Average Score: 0.96 	 current mean: 1.17	 Min:0.08	Max:3.60	Duration:16.18
	Episode 4	Average Score: 0.98 	 current mean: 1.01	 Min:0.00	Max:2.04	Duration:15.92
	Episode 5	Average Score: 1.02 	 current mean: 1.20	 Min:0.00	Max:2.89	Duration:16.76
	Episode 6	Average Score: 1.18 	 current mean: 1.97	 Min:0.70	Max:3.60	Duration:19.73
	Episode 7	Average Score: 1.50 	 current mean: 3.44	 Min:1.26	Max:11.50	Duration:16.52
	Episode 8	Average Score: 1.93 	 current mean: 4.96	 Min:1.63	Max:11.34	Duration:17.04
	Episode 9	Average Score: 2.61 	 current mean: 8.04	 Min:3.13	Max:14.94	Duration:17.22
	Episode 10	Average Score: 3.80 	 current mean: 14.47	 Min:3.72	Max:23.72	Duration:18.01
	Episode 11	Average Score: 5.23 	 current mean: 19.50	 Min:7.81	Max:32.39	Duration:18.13
	Episode 12	Average Score: 6.47 	 current mean: 20.18	 Min:5.80	Max:28.38	Duration:18.95
	Episode 13	Average Score: 7.72 	 current mean: 22.66	 Min:10.10	Max:34.72	Duration:18.69
	Episode 14	Average Score: 9.08 	 current mean: 26.85	 Min:13.91	Max:38.62	Duration:18.82
	Episode 15	Average Score: 10.58 	 current mean: 31.54	 Min:16.88	Max:38.22	Duration:19.19
	Episode 16	Average Score: 11.91 	 current mean: 31.85	 Min:17.90	Max:38.55	Duration:19.12
	Episode 17	Average Score: 13.23 	 current mean: 34.31	 Min:14.91	Max:39.62	Duration:19.39
	Episode 18	Average Score: 14.40 	 current mean: 34.35	 Min:15.44	Max:39.42	Duration:20.17
	Episode 19	Average Score: 15.60 	 current mean: 37.20	 Min:21.99	Max:39.61	Duration:20.66
	Episode 20	Average Score: 16.57 	 current mean: 34.94	 Min:19.00	Max:39.64	Duration:21.49
	Episode 21	Average Score: 17.55 	 current mean: 37.13	 Min:19.04	Max:39.62	Duration:21.23
	Episode 22	Average Score: 18.47 	 current mean: 37.84	 Min:25.15	Max:39.57	Duration:21.75
	Episode 23	Average Score: 19.33 	 current mean: 38.37	 Min:36.40	Max:39.53	Duration:22.33
	Episode 24	Average Score: 20.12 	 current mean: 38.17	 Min:26.54	Max:39.41	Duration:22.86
	Episode 25	Average Score: 20.82 	 current mean: 37.66	 Min:26.61	Max:39.40	Duration:21.45
	Episode 26	Average Score: 21.44 	 current mean: 36.86	 Min:29.00	Max:39.34	Duration:21.90
	Episode 27	Average Score: 21.95 	 current mean: 35.33	 Min:24.03	Max:39.47	Duration:20.95
	Episode 28	Average Score: 22.45 	 current mean: 35.86	 Min:27.41	Max:39.36	Duration:21.43
	Episode 29	Average Score: 22.88 	 current mean: 34.80	 Min:29.60	Max:39.28	Duration:21.43
	Episode 30	Average Score: 23.21 	 current mean: 32.80	 Min:21.14	Max:39.33	Duration:21.85
	Episode 31	Average Score: 23.59 	 current mean: 35.11	 Min:29.51	Max:39.44	Duration:23.22
	Episode 32	Average Score: 23.87 	 current mean: 32.67	 Min:12.74	Max:37.72	Duration:23.62
	Episode 33	Average Score: 24.19 	 current mean: 34.20	 Min:31.26	Max:38.00	Duration:23.09
	Episode 34	Average Score: 24.51 	 current mean: 35.33	 Min:28.03	Max:38.77	Duration:23.28
	Episode 35	Average Score: 24.82 	 current mean: 35.26	 Min:26.75	Max:37.59	Duration:23.24
	Episode 36	Average Score: 25.14 	 current mean: 36.35	 Min:33.34	Max:38.74	Duration:23.66
	Episode 37	Average Score: 25.39 	 current mean: 34.48	 Min:20.22	Max:39.30	Duration:24.66
	Episode 38	Average Score: 25.63 	 current mean: 34.55	 Min:25.49	Max:38.37	Duration:23.82
	Episode 39	Average Score: 25.88 	 current mean: 35.23	 Min:27.46	Max:39.24	Duration:23.85
	Episode 40	Average Score: 26.13 	 current mean: 35.95	 Min:29.16	Max:39.13	Duration:24.04
	Episode 41	Average Score: 26.39 	 current mean: 36.81	 Min:29.51	Max:39.25	Duration:25.28
	Episode 42	Average Score: 26.65 	 current mean: 37.27	 Min:33.56	Max:39.26	Duration:26.21
	Episode 43	Average Score: 26.86 	 current mean: 35.41	 Min:28.47	Max:39.07	Duration:26.19
	Episode 44	Average Score: 27.00 	 current mean: 33.25	 Min:26.90	Max:36.96	Duration:27.19
	Episode 45	Average Score: 27.17 	 current mean: 34.71	 Min:27.23	Max:37.79	Duration:26.75
	Episode 46	Average Score: 27.33 	 current mean: 34.62	 Min:29.07	Max:39.36	Duration:26.80
	Episode 47	Average Score: 27.46 	 current mean: 33.32	 Min:19.93	Max:39.07	Duration:27.69
	Episode 48	Average Score: 27.62 	 current mean: 35.05	 Min:25.97	Max:39.54	Duration:27.97
	Episode 49	Average Score: 27.81 	 current mean: 37.02	 Min:33.06	Max:39.09	Duration:28.34
	Episode 50	Average Score: 27.99 	 current mean: 36.62	 Min:29.72	Max:39.57	Duration:28.14
	Episode 51	Average Score: 28.13 	 current mean: 35.49	 Min:27.56	Max:38.96	Duration:27.29
	Episode 52	Average Score: 28.30 	 current mean: 36.71	 Min:32.29	Max:39.50	Duration:30.01
	Episode 53	Average Score: 28.44 	 current mean: 35.60	 Min:28.39	Max:38.49	Duration:35.86
	Episode 54	Average Score: 28.58 	 current mean: 35.93	 Min:30.89	Max:39.21	Duration:37.90
	Episode 55	Average Score: 28.74 	 current mean: 37.86	 Min:33.51	Max:39.50	Duration:37.62
	Episode 56	Average Score: 28.92 	 current mean: 38.31	 Min:35.63	Max:39.55	Duration:36.69
	Episode 57	Average Score: 29.07 	 current mean: 37.55	 Min:34.73	Max:38.93	Duration:43.12
	Episode 58	Average Score: 29.21 	 current mean: 37.45	 Min:30.43	Max:39.54	Duration:46.21
	Episode 59	Average Score: 29.35 	 current mean: 37.18	 Min:34.20	Max:39.34	Duration:43.77
	Episode 60	Average Score: 29.45 	 current mean: 35.63	 Min:30.73	Max:39.66	Duration:45.84
	Episode 61	Average Score: 29.55 	 current mean: 35.53	 Min:29.79	Max:39.03	Duration:46.20
	Episode 62	Average Score: 29.60 	 current mean: 32.50	 Min:26.90	Max:38.14	Duration:44.15
	Episode 63	Average Score: 29.66 	 current mean: 33.66	 Min:18.72	Max:37.85	Duration:45.33
	Episode 64	Average Score: 29.71 	 current mean: 32.85	 Min:25.40	Max:36.15	Duration:44.70
	Episode 65	Average Score: 29.75 	 current mean: 32.04	 Min:24.83	Max:35.95	Duration:43.84
	Episode 66	Average Score: 29.79 	 current mean: 32.28	 Min:25.89	Max:36.98	Duration:45.64
	Episode 67	Average Score: 29.82 	 current mean: 31.68	 Min:26.13	Max:35.88	Duration:44.03
	Episode 68	Average Score: 29.81 	 current mean: 29.42	 Min:25.31	Max:36.14	Duration:47.04
	Episode 69	Average Score: 29.86 	 current mean: 33.50	 Min:27.80	Max:39.38	Duration:47.06
	Episode 70	Average Score: 29.88 	 current mean: 31.11	 Min:21.69	Max:38.79	Duration:46.42
	Episode 71	Average Score: 29.81 	 current mean: 24.53	 Min:16.88	Max:39.19	Duration:46.04
	Episode 72	Average Score: 29.77 	 current mean: 27.23	 Min:15.29	Max:37.62	Duration:45.44
	Episode 73	Average Score: 29.74 	 current mean: 27.76	 Min:21.82	Max:33.71	Duration:46.08
	Episode 74	Average Score: 29.72 	 current mean: 28.01	 Min:22.91	Max:31.51	Duration:49.20
	Episode 75	Average Score: 29.70 	 current mean: 28.15	 Min:15.37	Max:35.38	Duration:44.91
	Episode 76	Average Score: 29.66 	 current mean: 26.66	 Min:11.66	Max:32.64	Duration:46.67
	Episode 77	Average Score: 29.62 	 current mean: 26.87	 Min:17.07	Max:37.28	Duration:45.40
	Episode 78	Average Score: 29.60 	 current mean: 27.65	 Min:19.59	Max:39.45	Duration:44.01
	Episode 79	Average Score: 29.58 	 current mean: 28.08	 Min:17.13	Max:34.41	Duration:41.84
	Episode 80	Average Score: 29.51 	 current mean: 24.26	 Min:13.80	Max:31.66	Duration:32.10
	Episode 81	Average Score: 29.50 	 current mean: 28.43	 Min:17.69	Max:39.42	Duration:32.51
	Episode 82	Average Score: 29.49 	 current mean: 28.81	 Min:12.68	Max:36.98	Duration:31.02
	Episode 83	Average Score: 29.49 	 current mean: 29.70	 Min:19.64	Max:33.18	Duration:31.03
	Episode 84	Average Score: 29.49 	 current mean: 29.05	 Min:18.75	Max:34.17	Duration:31.35
	Episode 85	Average Score: 29.48 	 current mean: 28.74	 Min:17.41	Max:34.54	Duration:31.19
	Episode 86	Average Score: 29.47 	 current mean: 29.19	 Min:15.55	Max:35.06	Duration:29.59
	Episode 87	Average Score: 29.38 	 current mean: 21.42	 Min:14.72	Max:30.18	Duration:30.74
	Episode 88	Average Score: 29.31 	 current mean: 23.21	 Min:16.51	Max:32.94	Duration:33.01
	Episode 89	Average Score: 29.26 	 current mean: 25.10	 Min:19.37	Max:31.00	Duration:35.05
	Episode 90	Average Score: 29.16 	 current mean: 20.22	 Min:11.84	Max:26.52	Duration:35.33
	Episode 91	Average Score: 29.11 	 current mean: 23.89	 Min:13.85	Max:30.51	Duration:34.81
	Episode 92	Average Score: 28.99 	 current mean: 18.60	 Min:5.21	Max:26.73	Duration:34.70
	Episode 93	Average Score: 28.86 	 current mean: 16.48	 Min:8.36	Max:24.02	Duration:33.28
	Episode 94	Average Score: 28.73 	 current mean: 16.96	 Min:5.86	Max:25.23	Duration:35.82
	Episode 95	Average Score: 28.57 	 current mean: 13.41	 Min:0.00	Max:24.72	Duration:34.92
	Episode 96	Average Score: 28.40 	 current mean: 12.65	 Min:3.81	Max:19.94	Duration:34.83
	Episode 97	Average Score: 28.27 	 current mean: 15.73	 Min:4.13	Max:25.14	Duration:34.87
	Episode 98	Average Score: 28.17 	 current mean: 18.60	 Min:10.65	Max:23.81	Duration:35.85
	Episode 99	Average Score: 28.10 	 current mean: 20.86	 Min:13.10	Max:26.97	Duration:35.43
	Episode 100	Average Score: 28.06 	 current mean: 24.30	 Min:14.70	Max:29.94	Duration:39.94
	Episode 101	Average Score: 28.25 	 current mean: 20.12	 Min:3.95	Max:27.93	Duration:39.70
	Episode 102	Average Score: 28.43 	 current mean: 18.90	 Min:1.18	Max:26.10	Duration:36.90
	Episode 103	Average Score: 28.66 	 current mean: 24.19	 Min:9.71	Max:30.53	Duration:34.64
	Episode 104	Average Score: 28.91 	 current mean: 26.01	 Min:18.25	Max:32.58	Duration:35.97
	Episode 105	Average Score: 29.19 	 current mean: 28.70	 Min:23.77	Max:33.01	Duration:37.23
	Episode 106	Average Score: 29.41 	 current mean: 24.25	 Min:13.89	Max:31.63	Duration:35.35
	Episode 107	Average Score: 29.65 	 current mean: 27.35	 Min:17.31	Max:33.40	Duration:34.10
	Episode 108	Average Score: 29.93 	 current mean: 32.42	 Min:23.90	Max:37.18	Duration:34.99
	Episode 109	Average Score: 30.18 	 current mean: 33.15	 Min:27.35	Max:39.39	Duration:36.06

Environment solved in 109 episodes!