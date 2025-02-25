-- 插入用户数据
alter table user auto_increment = 1;

INSERT INTO `user` (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `nickname`, `gender`, `phone`, `is_ban`, `role`, `balance`)
VALUES
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 1, 'admin', '管理员', '李', 'admin@example.com', 1, 1, '2025-02-23 10:00:00', '超级管理员', 1, '13812345678', 0, 'admin', 1000.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'wangkaiwen', '王凯文', '王', 'xiaoming@example.com', 1, 1, '2025-02-22 15:30:00', '凯文', 1, '13887654321', 0, 'general', 150.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'zhaoshanshan', '赵珊珊', '赵', 'xiaohong@example.com', 1, 1, '2025-02-21 14:00:00', '珊珊', 0, '13912345678', 0, 'general', 200.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'chenchenxi', '陈晨曦', '陈', 'lisa@example.com', 1, 1, '2025-02-20 09:00:00', '晨曦', 0, '13987654321', 0, 'general', 300.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'zhangweibo', '张伟博', '张', 'jerry@example.com', 1, 1, '2025-02-19 08:30:00', '伟博', 1, '13712345678', 0, 'general', 400.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'liujingyi', '刘婧怡', '刘', 'peter@example.com', 1, 1, '2025-02-18 07:45:00', '婧怡', 1, '13787654321', 0, 'general', 500.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'huangziqi', '黄子琪', '黄', 'lily@example.com', 1, 1, '2025-02-17 10:15:00', '子琪', 1, '13612345678', 0, 'designer', 600.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'yangfangyu', '杨芳瑜', '杨', 'tom@example.com', 1, 1, '2025-02-16 12:00:00', '芳瑜', 0, '13687654321', 0, 'designer', 700.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'liujunjie', '刘俊杰', '刘', 'grace@example.com', 1, 1, '2025-02-15 11:00:00', '俊杰', 1, '13512345678', 0, 'designer', 800.00),
('pbkdf2_sha256$600000$ZGdcvUGyH5vutRzCm7pm4h$7HWM2FDNOThWuBqEYr3O+6UJyPcLAGiOKvirofTCQ3Q=', NULL, 0, 'zhouzixuan', '周子轩', '周', 'winston@example.com', 1, 1, '2025-02-14 10:30:00', '子轩', 0, '13587654321', 0, 'designer', 900.00);



-- 插入画稿数据
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (1, '奇幻世界的探险', '这幅画展现了一个充满神秘生物和绚丽风景的仙境。在画面中可以看到，奇异的植物与壮观的山脉交相辉映，天空中漂浮着形状奇特的云朵，以及一些无法用言语形容的神秘生物在这片神奇的土地上自由地生活着。此景让人仿佛置身于一个未曾有人踏足的神秘领域，充满了探索的诱惑。', 'D:\\draft_image\\design/61ddfdd6-fba5-4136-b1e4-201d572a7729.png', '61ddfdd6-fba5-4136-b1e4-201d572a7729.png', 126, 1, 7, '', 1740453305, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (2, '夜幕下的未来都市', '在这幅画中，展示了一个灯火辉煌的未来城市夜景。高楼大厦之间，飞行汽车穿梭其中，与静谧的夜空形成了鲜明的对比。城市的每一个角落都被霓虹灯装饰得五彩斑斓，显示着这个时代的繁荣和科技的进步。这不仅是一个关于未来的想象，也是对科技进步无限可能性的一种赞美。', 'D:\\draft_image\\design/06d95742-35ae-48d2-a7ac-4dc0f0c0baa8.png', '06d95742-35ae-48d2-a7ac-4dc0f0c0baa8.png', 125, 4, 7, '', 1740453520, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (3, '梦幻之海', '这幅画展示了珊瑚礁和各种奇异的海洋生物在清澈见底的海水中自由游弋的场景。绚丽多彩的珊瑚、优雅游动的鱼群以及神秘莫测的海底环境构成了这个令人神往的梦幻海洋世界。', 'D:\\draft_image\\design/f6e3f273-15dd-4560-be2a-0e29ab59052a.png', 'f6e3f273-15dd-4560-be2a-0e29ab59052a.png', 100, 4, 7, '', 1740453578, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (4, '知识的宝库', '这幅画描绘了一个古老的图书馆，高耸的书架上摆满了古籍。柔和的光线透过巨大的窗户洒落在布满灰尘的书籍上，营造出一种神秘而宁静的氛围。这里是知识与历史交织的地方，等待着人们去发掘那些被遗忘的故事。', 'D:\\draft_image\\design/e8d41a2f-f28d-4e01-a329-533cc8dad9f8.png', 'e8d41a2f-f28d-4e01-a329-533cc8dad9f8.png', 200, 1, 7, '', 1740453610, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (5, '星际漫游者', '展示了一名宇航员在星际间漂浮的场景，背景是绚烂的星云和遥远的行星。浩瀚宇宙中的孤独与美丽在这里得到了完美的体现，让人感受到人类对未知世界的无尽好奇与探索精神。', 'D:\\draft_image\\design/84bffcd7-06e5-4c61-992d-34f4d09cd5de.png', '84bffcd7-06e5-4c61-992d-34f4d09cd5de.png', 130, 1, 10, '', 1740453690, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (6, '宇宙神秘之地', '这幅画将带我们进入宇宙深处的一个神秘星球，那里有着奇异的地貌和未知的生命形式。想象一下，在遥远的银河系边缘，有一颗被多彩极光覆盖的行星，其表面是未被探索的广阔荒野和闪烁着微光的湖泊。', 'D:\\draft_image\\design/364628c5-7ec1-45b4-baad-70a6436a184e.png', '364628c5-7ec1-45b4-baad-70a6436a184e.png', 200, 1, 10, '', 1740454395, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (7, '未来都市夜景', '未来都市的夜景，霓虹灯照亮了高楼大厦的轮廓，飞行汽车穿梭其中，充分展现了科技感与现代气息', 'D:\\draft_image\\design/011c4c47-ae0b-4b45-bb75-0e5cf0a6d4d8.png', '011c4c47-ae0b-4b45-bb75-0e5cf0a6d4d8.png', 70, 4, 10, '', 1740458240, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (8, '宁静海边小屋', '带我们来到了宁静的海边小屋，白天阳光温暖，夜晚星辰璀璨，海浪声带来无比的宁静和谐。', 'D:\\draft_image\\design/bb04028c-70d3-420f-94cc-fbd6c69493f3.png', 'bb04028c-70d3-420f-94cc-fbd6c69493f3.png', 90, 2, 10, '', 1740458273, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (9, '秋日森林漫步', '一片秋天的森林景象，地面上铺满了落叶，树木呈现出红黄色调。阳光透过树叶洒下，为整个场景增添了一丝温暖和宁静，仿佛能感受到秋天的气息。', 'D:\\draft_image\\design/2d5c34a7-e08e-447c-92c8-508572524156.png', '2d5c34a7-e08e-447c-92c8-508572524156.png', 68, 1, 10, '', 1740458340, 0);
INSERT INTO `draft`.`draft` (`id`, `title`, `description`, `image_url`, `image_name`, `price`, `category_id`, `designer_id`, `status`, `online_time`, `is_outline`) VALUES (10, '古老城堡遗迹', '一个位于山顶上的古老城堡废墟，被茂密的森林环绕，夜晚明月高悬，给这座城堡增添了一份神秘色彩，仿佛它承载着无数往昔的故事。', 'D:\\draft_image\\design/5c27f5bf-9c26-4682-bd46-d50d92506830.png', '5c27f5bf-9c26-4682-bd46-d50d92506830.png', 35, 1, 10, '', 1740458383, 0);
