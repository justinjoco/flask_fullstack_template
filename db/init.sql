CREATE TABLE IF NOT EXISTS item (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    count BIGINT NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS item_name_idx ON item(name);

CREATE TABLE IF NOT EXISTS "order" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(255) NOT NULL,
    order_price DECIMAL(10,2),
    date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS "item_order" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID REFERENCES "order"(id) NOT NULL,
    item_id UUID REFERENCES item(id) NOT NULL,
    amount_bought BIGINT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
INSERT INTO item(name, price, count) VALUES('Cards', 1.00, 5);
INSERT INTO item(name, price, count) VALUES('Soap', 3.00, 4);
INSERT INTO item(name, price, count) VALUES('Broom', 2.50, 2);
INSERT INTO item(name, price, count) VALUES('Tissues', 3.25, 10);
