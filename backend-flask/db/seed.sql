-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Abheeshek Jain', 'abheedjain@gmail.com','equinox9.in' ,'MOCK'),
  ('Andrew Bayko', 'bayko@exampro.co', 'bayko' ,'MOCK'),
  ('Londo Mollari', 'lmollari@centari.co', 'londo' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'equinox9.in' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )