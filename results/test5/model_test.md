## Hyper parameters used:
	batch_size=1024
	buffer_size=524288
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
	weight_decay=1e-05

##Training stats:
	Episode 1	Average Score: 0.40 	 current mean: 0.40	 Min:0.08	Max:1.33	Duration:21.48
	Episode 2	Average Score: 0.35 	 current mean: 0.31	 Min:0.05	Max:0.68	Duration:21.91
	Episode 3	Average Score: 0.47 	 current mean: 0.69	 Min:0.18	Max:2.59	Duration:19.79
	Episode 4	Average Score: 0.52 	 current mean: 0.69	 Min:0.00	Max:1.50	Duration:27.52
	Episode 5	Average Score: 0.52 	 current mean: 0.54	 Min:0.14	Max:0.91	Duration:30.63
	Episode 6	Average Score: 0.48 	 current mean: 0.23	 Min:0.00	Max:1.02	Duration:23.18
	Episode 7	Average Score: 0.49 	 current mean: 0.56	 Min:0.02	Max:1.93	Duration:21.61
	Episode 8	Average Score: 0.69 	 current mean: 2.08	 Min:0.17	Max:6.15	Duration:23.17
	Episode 9	Average Score: 0.91 	 current mean: 2.67	 Min:1.29	Max:4.65	Duration:21.10
	Episode 10	Average Score: 1.11 	 current mean: 3.00	 Min:0.68	Max:6.76	Duration:22.34
	Episode 11	Average Score: 1.47 	 current mean: 5.02	 Min:0.00	Max:8.25	Duration:24.78
	Episode 12	Average Score: 2.26 	 current mean: 10.99	 Min:4.90	Max:33.48	Duration:25.74
	Episode 13	Average Score: 3.14 	 current mean: 13.73	 Min:1.46	Max:31.35	Duration:26.59
	Episode 14	Average Score: 3.86 	 current mean: 13.16	 Min:2.44	Max:23.06	Duration:27.65
	Episode 15	Average Score: 4.78 	 current mean: 17.59	 Min:7.45	Max:30.09	Duration:28.54
	Episode 16	Average Score: 5.72 	 current mean: 19.82	 Min:8.40	Max:31.85	Duration:29.01
	Episode 17	Average Score: 6.38 	 current mean: 17.06	 Min:5.33	Max:25.57	Duration:29.52
	Episode 18	Average Score: 6.99 	 current mean: 17.35	 Min:6.49	Max:28.38	Duration:29.17
	Episode 19	Average Score: 7.89 	 current mean: 23.99	 Min:6.29	Max:35.96	Duration:29.86
	Episode 20	Average Score: 8.52 	 current mean: 20.53	 Min:6.33	Max:27.91	Duration:32.27
	Episode 21	Average Score: 9.11 	 current mean: 20.86	 Min:7.22	Max:29.11	Duration:32.25
	Episode 22	Average Score: 9.68 	 current mean: 21.60	 Min:5.69	Max:31.52	Duration:32.15
	Episode 23	Average Score: 10.32 	 current mean: 24.48	 Min:15.74	Max:33.74	Duration:32.95
	Episode 24	Average Score: 10.88 	 current mean: 23.79	 Min:13.37	Max:35.98	Duration:32.36
	Episode 25	Average Score: 11.39 	 current mean: 23.75	 Min:7.09	Max:35.55	Duration:34.56
	Episode 26	Average Score: 11.95 	 current mean: 25.88	 Min:12.02	Max:39.54	Duration:33.29
	Episode 27	Average Score: 12.48 	 current mean: 26.26	 Min:8.32	Max:38.40	Duration:33.58
	Episode 28	Average Score: 13.11 	 current mean: 30.14	 Min:16.95	Max:37.95	Duration:35.26
	Episode 29	Average Score: 13.61 	 current mean: 27.57	 Min:17.47	Max:36.99	Duration:34.11
	Episode 30	Average Score: 13.90 	 current mean: 22.35	 Min:7.98	Max:37.35	Duration:35.05
	Episode 31	Average Score: 14.22 	 current mean: 23.90	 Min:6.01	Max:37.63	Duration:34.79
	Episode 32	Average Score: 14.65 	 current mean: 27.82	 Min:11.43	Max:37.93	Duration:33.31
	Episode 33	Average Score: 15.10 	 current mean: 29.56	 Min:8.13	Max:38.52	Duration:34.65
	Episode 34	Average Score: 15.37 	 current mean: 24.18	 Min:9.58	Max:37.20	Duration:33.73
	Episode 35	Average Score: 15.71 	 current mean: 27.41	 Min:8.46	Max:39.45	Duration:35.09
	Episode 36	Average Score: 15.98 	 current mean: 25.35	 Min:4.41	Max:35.48	Duration:35.49
	Episode 37	Average Score: 16.23 	 current mean: 25.03	 Min:7.24	Max:37.24	Duration:35.55
	Episode 38	Average Score: 16.44 	 current mean: 24.30	 Min:6.89	Max:37.38	Duration:34.63
	Episode 39	Average Score: 16.64 	 current mean: 24.29	 Min:8.64	Max:38.20	Duration:33.56
	Episode 40	Average Score: 16.93 	 current mean: 28.29	 Min:5.82	Max:39.47	Duration:35.04
	Episode 41	Average Score: 17.23 	 current mean: 29.23	 Min:15.59	Max:36.32	Duration:34.26
	Episode 42	Average Score: 17.51 	 current mean: 29.02	 Min:10.04	Max:38.83	Duration:33.34
	Episode 43	Average Score: 17.82 	 current mean: 30.80	 Min:27.22	Max:39.33	Duration:33.38
	Episode 44	Average Score: 17.97 	 current mean: 24.61	 Min:16.95	Max:32.59	Duration:35.17
	Episode 45	Average Score: 18.19 	 current mean: 27.73	 Min:12.45	Max:38.86	Duration:35.23
	Episode 46	Average Score: 18.34 	 current mean: 24.92	 Min:14.71	Max:35.36	Duration:34.61
	Episode 47	Average Score: 18.47 	 current mean: 24.68	 Min:0.13	Max:33.50	Duration:34.57
	Episode 48	Average Score: 18.63 	 current mean: 26.06	 Min:17.56	Max:37.77	Duration:34.17
	Episode 49	Average Score: 18.78 	 current mean: 25.86	 Min:20.50	Max:29.62	Duration:37.30
	Episode 50	Average Score: 18.97 	 current mean: 28.57	 Min:22.85	Max:34.87	Duration:35.52
	Episode 51	Average Score: 19.21 	 current mean: 31.13	 Min:24.51	Max:34.96	Duration:35.55
	Episode 52	Average Score: 19.41 	 current mean: 29.22	 Min:13.06	Max:35.14	Duration:35.78
	Episode 53	Average Score: 19.57 	 current mean: 27.92	 Min:13.40	Max:36.55	Duration:34.73
	Episode 54	Average Score: 19.76 	 current mean: 29.79	 Min:23.93	Max:38.36	Duration:35.68
	Episode 55	Average Score: 19.96 	 current mean: 31.20	 Min:21.69	Max:37.08	Duration:34.21
	Episode 56	Average Score: 20.17 	 current mean: 31.78	 Min:19.30	Max:37.36	Duration:34.98
	Episode 57	Average Score: 20.38 	 current mean: 32.03	 Min:24.82	Max:36.76	Duration:35.49
	Episode 58	Average Score: 20.58 	 current mean: 31.66	 Min:18.88	Max:36.79	Duration:34.78
	Episode 59	Average Score: 20.73 	 current mean: 29.82	 Min:22.79	Max:34.79	Duration:33.66
	Episode 60	Average Score: 20.89 	 current mean: 29.99	 Min:24.12	Max:35.48	Duration:33.59
	Episode 61	Average Score: 20.99 	 current mean: 27.08	 Min:17.74	Max:39.30	Duration:35.76
	Episode 62	Average Score: 21.08 	 current mean: 26.75	 Min:20.61	Max:31.03	Duration:34.04
	Episode 63	Average Score: 21.14 	 current mean: 24.92	 Min:15.38	Max:39.43	Duration:32.69
	Episode 64	Average Score: 21.15 	 current mean: 21.62	 Min:14.27	Max:28.25	Duration:33.14
	Episode 65	Average Score: 21.19 	 current mean: 23.46	 Min:13.78	Max:28.79	Duration:31.75
	Episode 66	Average Score: 21.19 	 current mean: 21.27	 Min:3.89	Max:30.94	Duration:31.94
	Episode 67	Average Score: 21.12 	 current mean: 16.49	 Min:3.23	Max:27.35	Duration:32.19
	Episode 68	Average Score: 21.00 	 current mean: 13.14	 Min:2.16	Max:26.16	Duration:31.50
	Episode 69	Average Score: 20.90 	 current mean: 14.39	 Min:2.48	Max:35.22	Duration:32.64
	Episode 70	Average Score: 20.76 	 current mean: 10.65	 Min:1.29	Max:29.48	Duration:33.26
	Episode 71	Average Score: 20.74 	 current mean: 19.74	 Min:4.88	Max:35.42	Duration:32.99
	Episode 72	Average Score: 20.70 	 current mean: 17.77	 Min:1.03	Max:34.24	Duration:29.57
	Episode 73	Average Score: 20.68 	 current mean: 19.25	 Min:8.84	Max:32.98	Duration:31.93
	Episode 74	Average Score: 20.63 	 current mean: 16.60	 Min:3.57	Max:29.52	Duration:34.59
	Episode 75	Average Score: 20.54 	 current mean: 14.47	 Min:4.69	Max:29.67	Duration:37.68
	Episode 76	Average Score: 20.52 	 current mean: 18.58	 Min:6.58	Max:31.71	Duration:35.41
	Episode 77	Average Score: 20.55 	 current mean: 22.74	 Min:5.80	Max:39.21	Duration:34.39
	Episode 78	Average Score: 20.51 	 current mean: 17.90	 Min:5.63	Max:34.82	Duration:35.29
	Episode 79	Average Score: 20.50 	 current mean: 19.79	 Min:6.23	Max:36.42	Duration:34.57
	Episode 80	Average Score: 20.47 	 current mean: 17.75	 Min:8.52	Max:34.93	Duration:34.59
	Episode 81	Average Score: 20.46 	 current mean: 19.73	 Min:6.93	Max:28.93	Duration:34.21
	Episode 82	Average Score: 20.47 	 current mean: 21.16	 Min:6.87	Max:33.96	Duration:35.25
	Episode 83	Average Score: 20.43 	 current mean: 17.12	 Min:9.76	Max:26.73	Duration:34.76
	Episode 84	Average Score: 20.46 	 current mean: 22.83	 Min:13.75	Max:35.22	Duration:34.18
	Episode 85	Average Score: 20.50 	 current mean: 23.75	 Min:7.70	Max:34.04	Duration:35.23
	Episode 86	Average Score: 20.53 	 current mean: 22.99	 Min:9.99	Max:37.66	Duration:35.68
	Episode 87	Average Score: 20.56 	 current mean: 23.37	 Min:7.63	Max:33.18	Duration:35.68
	Episode 88	Average Score: 20.55 	 current mean: 20.24	 Min:2.88	Max:35.63	Duration:35.72
	Episode 89	Average Score: 20.56 	 current mean: 20.72	 Min:2.39	Max:33.95	Duration:35.87
	Episode 90	Average Score: 20.61 	 current mean: 25.22	 Min:5.76	Max:36.95	Duration:37.33
	Episode 91	Average Score: 20.64 	 current mean: 23.20	 Min:12.64	Max:33.36	Duration:35.68
	Episode 92	Average Score: 20.66 	 current mean: 23.11	 Min:11.19	Max:32.90	Duration:35.05
	Episode 93	Average Score: 20.70 	 current mean: 24.16	 Min:13.54	Max:37.84	Duration:39.68
	Episode 94	Average Score: 20.74 	 current mean: 24.60	 Min:14.71	Max:32.84	Duration:35.19
	Episode 95	Average Score: 20.81 	 current mean: 27.34	 Min:16.41	Max:35.87	Duration:35.53
	Episode 96	Average Score: 20.81 	 current mean: 20.61	 Min:8.19	Max:31.56	Duration:35.56
	Episode 97	Average Score: 20.77 	 current mean: 17.18	 Min:9.25	Max:22.70	Duration:34.86
	Episode 98	Average Score: 20.72 	 current mean: 15.33	 Min:8.47	Max:20.79	Duration:36.71
	Episode 99	Average Score: 20.65 	 current mean: 14.24	 Min:8.53	Max:20.44	Duration:35.72
	Episode 100	Average Score: 20.63 	 current mean: 18.65	 Min:9.30	Max:31.03	Duration:33.60
