PGDMP     7    1                 x            api    12.1    12.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16393    api    DATABASE     �   CREATE DATABASE api WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Venezuela.1252' LC_CTYPE = 'Spanish_Venezuela.1252';
    DROP DATABASE api;
                postgres    false            �            1259    24589    tasks    TABLE     �   CREATE TABLE public.tasks (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    description text NOT NULL,
    deadline timestamp without time zone NOT NULL,
    created_at timestamp without time zone NOT NULL
);
    DROP TABLE public.tasks;
       public         heap    postgres    false            �            1259    24587    tasks_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.tasks_id_seq;
       public          postgres    false    203            	           0    0    tasks_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;
          public          postgres    false    202            �
           2604    24592    tasks id    DEFAULT     d   ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);
 7   ALTER TABLE public.tasks ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    24589    tasks 
   TABLE DATA           M   COPY public.tasks (id, title, description, deadline, created_at) FROM stdin;
    public          postgres    false    203   �
       
           0    0    tasks_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.tasks_id_seq', 3, true);
          public          postgres    false    202            �
           2606    24597    tasks tasks_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_pkey;
       public            postgres    false    203               �   x���;�0k�{�X�"�PSQ�q��H�����>�OS��knwVgy�5?Z.�bd�7�8"n�R���.Dv�{���^]^�N�R���=7����i0��I��2�7��,S�΍Fk�I�7�     