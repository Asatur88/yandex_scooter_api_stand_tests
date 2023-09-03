

# Подсчет заказов в доставке для каждого курьера
SELECT
   c."login" AS courier_login, # Логин курьера
   COUNT(DISTINCT o.id) AS orders_in_delivery # Количество заказов в доставке
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true # Заказы в статусе "В доставке"
GROUP BY c."login";

# Определение статуса заказа на основе условий
SELECT
   track AS order_tracker, # Трекер заказа
   CASE
      WHEN finished = true THEN 2 # Статус 2: Завершен
      WHEN cancelled = true THEN -1 # Статус -1: Отменен
      WHEN "inDelivery" = true THEN 1 # Статус 1: В доставке
      ELSE 0 # Статус 0: Другой статус
   END AS order_status
FROM "Orders";

